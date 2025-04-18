import os
import re

from datetime import datetime
from models import (
    Account,
    AudioSettings,
    ColumnHeaders,
    TextClipInfo,
    TimeModifiers,
    VideoModes,
    VideoSettings,
    AdditionalVideoSettings,
)
from presets import Presets
from functions import create_video, fetch_chapter_name
from typing import Optional


class TikTok:
    def __init__(self, account: Account):
        self.account = account

    def create(
        self,
        preset: Optional[Presets] = None,
        video_verse_range: Optional[tuple[int, int]] = None,
        audio_directory_path: Optional[str] = None,
        time_modifiers: Optional[TimeModifiers] = None,
        video_settings: Optional[VideoSettings] = VideoSettings(
            allowDuplicateClips=False,
            allowMirroredClips=True,
            clipSpeed=1.0,
            minimumClipDuration=1.25,
            videoDimensions=(576, 1024),
            videoMode=VideoModes.VIDEO,
        ),
        additional_video_settings: Optional[AdditionalVideoSettings] = None,
        output_mp4_file: Optional[str] = None,
    ):
        if preset:
            audio_directory_path = preset.value.audio_directory_path
            video_verse_range = video_verse_range or preset.value.video_verse_range
            time_modifiers = time_modifiers or preset.value.time_modifiers
            additional_video_settings = (
                additional_video_settings
                or preset.value.additional_video_settings
                or AdditionalVideoSettings()
            )

        if isinstance(video_verse_range, int):
            video_verse_range = (video_verse_range, video_verse_range)

        for file in os.listdir(audio_directory_path):
            if file.endswith(".wav"):
                audio_file_path = os.path.join(audio_directory_path, file)
                break
        else:
            for file in os.listdir(audio_directory_path):
                if file.endswith(".mp3"):
                    audio_file_path = os.path.join(audio_directory_path, file)
                    break
            else:
                raise FileNotFoundError("No audio file found in the directory.")

        pattern = r"\d+"
        match = re.findall(pattern, audio_directory_path)

        chapter_number = int(match[0])
        start_to_end_timestamp_verse_range = (int(match[1]), int(match[-1]))

        audio_settings = AudioSettings(
            audioFile=audio_file_path,
            chapterNumber=chapter_number,
            verseRange=start_to_end_timestamp_verse_range,
        )

        if not isinstance(self.account, Account):
            account_name = str(self.account).split(".")[-1].lower()
            self.account = self.account.value
        else:
            account_name = "anonymous"

        language_abbreviation = self.account.language.value.abbreviation

        chapter_name = fetch_chapter_name(chapter_number)
        reciter_name = audio_directory_path.split("\\")[-2]
        try:
            start_verse, end_verse = video_verse_range
        except ValueError:
            start_verse = end_verse = video_verse_range
        verse_range = (
            f"{start_verse}-{end_verse}"
            if start_verse != end_verse
            else str(start_verse)
        )

        output_mp4_file_name = f"{chapter_name} ({chapter_number}.{verse_range}) - {reciter_name} {account_name} {language_abbreviation} {datetime.now().strftime('%d-%m-%Y %H.%M.%S')}"

        chapter_csv_file_path = os.path.join(audio_directory_path, "chapter.csv")
        timestamps_csv_file_path = os.path.join(audio_directory_path, "Markers.csv")

        csv_column_names = ColumnHeaders(
            verse_number="verse", verse_text="ar", timestamp="timestamps"
        )

        verse_text_text_clip = TextClipInfo(
            text_background_color="transparent",
            text_fade_duration=0.5,
            text_font_size=44,
            text_method="caption",
            text_position=("center", 0.41),
            text_size=(video_settings.videoDimensions[0] * 0.9, None),
        )

        verse_translation_text_clip = TextClipInfo(
            text_background_color="transparent",
            text_fade_duration=0.5,
            text_font_size=20,
            text_method="caption",
            text_position=("center", 0.49),
            text_size=(video_settings.videoDimensions[0] * 0.6, None),
        )

        verse_number_text_clip = TextClipInfo(
            text_background_color="transparent",
            text_fade_duration=0.5,
            text_font_size=20,
            text_method="caption",
            text_position=("center", 0.75),
            text_size=(video_settings.videoDimensions[0] * 0.6, None),
        )

        reciter_name = None if reciter_name.casefold() == "unknown" else reciter_name
        reciter_name_text_clip = TextClipInfo(
            text_background_color="transparent",
            text_fade_duration=0.5,
            text_font_size=20,
            text_method="caption",
            text_position=("center", 0.20),
            text_size=(video_settings.videoDimensions[0] * 0.6, None),
        )

        create_video(
            account=self.account,
            audioSettings=audio_settings,
            csvColumnNames=csv_column_names,
            timeModifiers=time_modifiers,
            videoSettings=video_settings,
            output_video_verse_range=video_verse_range,
            outputFileName=output_mp4_file_name,
            chapterCsvFile=chapter_csv_file_path,
            timestampsCsvFile=timestamps_csv_file_path,
            additionalVideoSettings=additional_video_settings,
            verse_text_text_clip=verse_text_text_clip,
            verse_translation_text_clip=verse_translation_text_clip,
            verse_number_text_clip=verse_number_text_clip,
            reciter_name=reciter_name,
            reciter_name_text_clip=reciter_name_text_clip,
            outputFile=output_mp4_file,
        )
