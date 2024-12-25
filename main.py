from models import Account, ColorModes, Languages, AdditionalVideoSettings
from moviepy.config import change_settings
from presets import Presets
from enum import Enum
from tiktok import TikTok
from enums import Accounts

change_settings(
    {"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"}
)


class Joe(Enum):
    hello = Account(
        clipDirectories=["Background_Clips/Anime"],
        language=Languages.ENGLISH,
        mode=ColorModes.DARK,
        verseTextFontFile="Fonts/Hafs.ttf",
        verseTranslationFontFile="Fonts/Butler_Regular.otf",
    )


def main():
    tiktok = TikTok(Accounts.QURAN_2_LISTEN)
    preset = Presets.MUHAMMAD_AL_LUHAIDAN_AL_AHZAB_40_44

    tiktok.create(
        preset,
        # additional_video_settings=AdditionalVideoSettings(video_map={}),
    )


if __name__ == "__main__":
    main()
