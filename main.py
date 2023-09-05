import cv2
import moviepy.editor as mpy
import os
import random
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style
from datetime import datetime
from enum import Enum
from plyer import notification
from pyquran import quran

ARABIC_FONT = "Fonts/Hafs.ttf"
ENGLISH_FONT = "Fonts/Butler_Regular.otf"

def colored_print(color: str, text: str):
    """
    Prints text in color

    Args:
        color (str): Colorama color
        text (str): Text to print
    """
    print(f"{color}{text}{Style.RESET_ALL}")

def get_time_difference_seconds(time1, time2):
        """
        Calculate the time difference between two time strings in the format "MM:SS.SSS"

        Args:
            time1 (str): The first time string
            time2 (str): The second time string

        Returns:
            float: The time difference in seconds
        """
        # Convert the time strings to timedelta objects
        time_format = "%M:%S.%f"
        time1 = datetime.strptime(time1, time_format)
        time2 = datetime.strptime(time2, time_format)
        
        # Calculate the time difference (subtraction)
        time_difference = abs(time2 - time1)

        # Convert the time difference to seconds as a float
        time_difference_seconds = time_difference.total_seconds()

        return time_difference_seconds

def create_notification(title, message):
        """
        Create a notification with the given parameters.

        Args:
            title (str): The title of the notification.
            message (str): The message of the notification.
        """
        notification.notify(
            title=title,
            message=message,
            app_name="Python",
            timeout=1
        )

def get_video_duration_seconds(video_path):
        """
        Get the duration of a video in seconds.

        Args:
            video_path (str): The path to the video file.

        Returns:
            float: The duration of the video in seconds.
        """
        video = cv2.VideoCapture(video_path)
        duration_seconds = video.get(cv2.CAP_PROP_FRAME_COUNT) / video.get(cv2.CAP_PROP_FPS)
        return duration_seconds

class TikTok:
    class MODES(Enum):
        DARK = 1
        LIGHT = 2
    
    def __init__(
            self,
            timestamps_csv_file_path: str,
            background_clips_directory_path: str,
            audio_file_path: str,
            output_file_path: str,
            mode: MODES = MODES.DARK,
            chapter_text_file_path: str = "chapter_text.txt",
            chapter_translation_file_path: str = "chapter_translation.txt",
            shadow_opacity: float = 0.7,
            text_fade_duration: float = 0.5,
            chapter: int = None,
            start_verse: int = None,
            end_verse: int = None
        ):
        if chapter_text_file_path == "chapter_text.txt" and chapter_translation_file_path == "chapter_translation.txt":
            if chapter < 1 or chapter > 114:
                colored_print(Fore.RED, "Chapter must be between 1 and 114")
                return
            self.chapter = chapter
            if end_verse < start_verse:
                colored_print(Fore.RED, "End verse must be greater than or equal to start verse")
                return
        self.start_verse = start_verse
        self.end_verse = end_verse
        self.timestamps_csv_file_path = timestamps_csv_file_path
        self.timestamps_txt_file_path = self.timestamps_csv_file_path.replace("Markers.csv", "timestamps.txt")
        self.background_clips_directory_path = background_clips_directory_path
        self.audio_file_path = audio_file_path
        self.output_file_path = output_file_path
        self.chapter_text_file_path = chapter_text_file_path
        self.chapter_translation_file_path = chapter_translation_file_path
        self.mode = mode
        if self.mode == TikTok.MODES.DARK:
            self.shadow_color = (0, 0, 0)
            self.verse_text_color = "rgb(255, 255, 255)"
            self.verse_translation_color = "rgb(255, 255, 255)"
        elif self.mode == TikTok.MODES.LIGHT:
            self.shadow_color = (255, 255, 255)
            self.verse_text_color = "rgb(0, 0, 0)"
            self.verse_translation_color = "rgb(0, 0, 0)"
        self.shadow_opacity = shadow_opacity
        self.text_fade_duration = text_fade_duration

    def create_video(self):
        try:
            self.create_timestamps_txt_file()
        except FileNotFoundError:
            colored_print(Fore.RED, "timestamps.csv file not found")
            return

        if self.chapter_text_file_path == "chapter_text.txt" and self.chapter_translation_file_path == "chapter_translation.txt":
            with open(self.chapter_text_file_path, "w", encoding="utf-8") as chapter_text_file, \
            open(self.chapter_translation_file_path, "w", encoding="utf-8") as chapter_translation_file:
                verse_text = self.get_verse_text(self.start_verse)
                if verse_text is None:
                    return
                for current_verse in range(self.start_verse, self.end_verse + 1):
                    verse_text = self.get_verse_text(current_verse)
                    if verse_text is not None:
                        chapter_text_file.write(verse_text + "\n")
                        verse_translation = self.get_verse_translation(current_verse)
                        chapter_translation_file.write(verse_translation + "\n")
                    else:
                        break

            input("Appropriately edit text files now...")

        with open(self.chapter_text_file_path, "r", encoding="utf-8") as chapter_text_file, \
        open(self.chapter_translation_file_path, "r", encoding="utf-8") as chapter_translation_file, \
        open(self.timestamps_txt_file_path, "r", encoding="utf-8") as timestamps_file:
            chapter_text_lines = chapter_text_file.readlines()
            chapter_translation_lines = chapter_translation_file.readlines()
            timestamps_lines = timestamps_file.readlines()
            used_background_clips = []
            video_clips = []
            for i in range(1, len(chapter_text_lines) + 1):
                verse_text = chapter_text_lines[i - 1].strip()
                verse_translation = chapter_translation_lines[i - 1].strip()
                audio_start = timestamps_lines[i - 1].strip().split(",")[0]
                audio_end = timestamps_lines[i].strip().split(",")[0]
                try:
                    text_end = timestamps_lines[i].strip().split(",")[1]
                except IndexError:
                    text_end = None
                video_clip_duration = get_time_difference_seconds(audio_start, audio_end)
                text_duration = get_time_difference_seconds(audio_start, text_end) if text_end is not None else None
                all_background_clips = [clip for clip in os.listdir(self.background_clips_directory_path) if clip.endswith(".mp4")]
                while True:
                    background_clip = random.choice(all_background_clips)
                    background_clip_path = os.path.join(self.background_clips_directory_path, background_clip)
                    background_clip_duration = get_video_duration_seconds(background_clip_path)
                    if background_clip not in used_background_clips and background_clip_duration >= video_clip_duration:
                        used_background_clips.append(background_clip)
                        break
                
                colored_print(Fore.GREEN, f"Creating clip {i}...")
                video_clip = self.create_video_clip(
                    background_clip_path=background_clip_path,
                    background_clip_duration=video_clip_duration,
                    text_duration=text_duration,
                    verse_text=verse_text,
                    verse_translation=verse_translation
                )
                video_clips.append(video_clip)
            final_video_start = timestamps_lines[0].strip().split(",")[0]
            final_video_end = timestamps_lines[-1].strip().split(",")[0]
            final_video_duration = get_time_difference_seconds(final_video_start, final_video_end)
            final_video = mpy.concatenate_videoclips(
                clips=video_clips,
                method="compose"
            ).set_audio(
                mpy.AudioFileClip(self.audio_file_path).subclip(final_video_start, final_video_end)
            ).set_duration(
                final_video_duration
            )
            colored_print(Fore.GREEN, "Creating final video...")
            final_video.write_videofile(
                self.output_file_path,
                codec="libx264",
                audio_codec="aac"
            )

            create_notification(
                title="TikTok",
                message="Video successfully created!"
            )

    def create_video_clip(self, background_clip_path, background_clip_duration, text_duration, verse_text, verse_translation):
        video_clip = mpy.VideoFileClip(background_clip_path)

        x_offset = random.randint(0, max(0, video_clip.w - 603))
        y_offset = random.randint(0, max(0, video_clip.h - 1072))

        video_clip = video_clip.set_duration(
            background_clip_duration
        ).crop(
            x1=x_offset,
            y1=y_offset,
            x2=x_offset + 603,
            y2=y_offset + 1072
        )

        shadow_clip = mpy.ColorClip(
            size=video_clip.size,
            color=self.shadow_color,
            duration=video_clip.duration
        ).set_opacity(
            self.shadow_opacity
        )

        video_with_shadow = mpy.CompositeVideoClip(
            [
                video_clip,
                shadow_clip
            ], 
            use_bgclip=True
        )

        text_duration = background_clip_duration if text_duration is None else text_duration

        verse_text_clip = mpy.TextClip(
            txt=verse_text,
            size=video_clip.size,
            color=self.verse_text_color,
            bg_color="transparent",
            fontsize=45,
            font=ARABIC_FONT
        ).set_position(
            (0, -.05), relative=True
        ).set_duration(
            text_duration
        ).crossfadein(
            self.text_fade_duration
        ).crossfadeout(
            self.text_fade_duration
        )

        verse_translation_clip = mpy.TextClip(
            txt=verse_translation,
            size=video_clip.size,
            color=self.verse_translation_color,
            bg_color="transparent",
            fontsize=18,
            font=ENGLISH_FONT
        ).set_position(
            (0, 0), relative=True
        ).set_duration(
            text_duration
        ).crossfadein(
            self.text_fade_duration
        ).crossfadeout(
            self.text_fade_duration
        )

        final_clip = mpy.CompositeVideoClip(
            [
                video_with_shadow,
                verse_text_clip,
                verse_translation_clip
            ], 
            use_bgclip=True
        ).set_duration(
            background_clip_duration
        ).set_fps(
            24
        )

        return final_clip

    def create_timestamps_txt_file(self):
        """
        Creates text file with timestamps from csv file with timestamps
        """
        with open(self.timestamps_csv_file_path, "r", encoding="utf-8") as csv_file:
            lines = csv_file.readlines()[1:]
            with open(self.timestamps_txt_file_path, "w", encoding="utf-8") as output_file:
                i = 0
                while i < len(lines):
                    time = lines[i].split("\t")[1]
                    type = lines[i].split("\t")[4]
                    if type == "Subclip":
                        i += 1
                        time2 = lines[i].split("\t")[1]
                        output_file.write(f"{time2},{time}\n")
                    else:
                        output_file.write(time)
                        if (i + 1) < len(lines):
                            output_file.write("\n")
                    i += 1
        colored_print(Fore.GREEN, f"Successfully created '{self.timestamps_txt_file_path}'")

    def get_verse_text(self, verse):
        """
        Gets the text of a verse from the Quran

        Args:
            verse (int): Verse number

        Returns:
            str: Verse text or None if verse not found
        """
        verse_text = quran.get_verse(self.chapter, verse, with_tashkeel=True)
        if verse_text is None or verse_text == "":
            colored_print(Fore.RED, f"Verse {verse} not found")
            return None
        return verse_text

    def get_verse_translation(self, verse):
        """
        Gets the translation of a verse from the Quran

        Args:
            verse (int): Verse number

        Returns:
            str: Verse translation or None if verse not found
        """
        try:
            response = requests.get(f"https://api.quran.com/api/v4/quran/translations/20?verse_key={self.chapter}:{verse}")
            translation = response.json()["translations"][0]["text"]
            soup = BeautifulSoup(translation, "html.parser")
            clean_text = soup.get_text()
            return clean_text
        except Exception as error:
            colored_print(Fore.RED, f"Error: {error}")
            return None

if __name__ == "__main__":
    tiktok = TikTok(
        timestamps_csv_file_path=r"Surahs\Abdul Rahman Mossad - 73 - Al-Muzzammil\Markers.csv",
        background_clips_directory_path=r"Background_Clips",
        audio_file_path=r"Surahs\Abdul Rahman Mossad - 73 - Al-Muzzammil\Abdul Rahman Mossad - 73 - Al-Muzzammil.mp3",
        output_file_path=r"Surahs\Abdul Rahman Mossad - 73 - Al-Muzzammil\Videos\1.mp4",
        mode=TikTok.MODES.LIGHT,
        chapter_text_file_path=r"Surahs\Abdul Rahman Mossad - 73 - Al-Muzzammil\chapter_text.txt",
        chapter_translation_file_path=r"Surahs\Abdul Rahman Mossad - 73 - Al-Muzzammil\chapter_translation.txt",
    )
    tiktok.create_video()