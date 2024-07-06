from classes import AdditionalVideoSettings, TimeModifiers
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


@dataclass
class Preset:
    audio_directory_path: str
    video_verse_range: tuple[int, int]
    time_modifiers: Optional[TimeModifiers] = field(
        default_factory=lambda: TimeModifiers(time_modifier=-0.2, end_time_modifier=0.0)
    )
    additional_video_settings: Optional[AdditionalVideoSettings] = field(
        default_factory=lambda: AdditionalVideoSettings()
    )

    def __post_init__(self):
        if isinstance(self.video_verse_range, int):
            self.video_verse_range = (self.video_verse_range, self.video_verse_range)


class Presets(Enum):
    TEST = Preset(
        r"Surahs\Unknown\Ar-Rahman (55.1-47)",
        (1, 47),
    )

    ABDUL_RAHMAN_MOSSAD_AL_ADIYAT_1_11 = Preset(r"Surahs\Abdul Rahman Mossad\Al-'Adiyat (100.1-11)", (1, 11))
    ABDUL_RAHMAN_MOSSAD_AL_ANKABUT_54_60 = Preset(
        r"Surahs\Abdul Rahman Mossad\Al-'Ankabut (29.53-64)",
        (54, 60),
        time_modifiers=TimeModifiers(time_modifier=-0.2, end_time_modifier=-0.4),
    )
    ABDUL_RAHMAN_MOSSAD_AL_ANKABUT_54_57 = Preset(
        r"Surahs\Abdul Rahman Mossad\Al-'Ankabut (29.53-64)",
        (54, 57),
        time_modifiers=TimeModifiers(time_modifier=-0.2, end_time_modifier=-0.2),
    )
    ABDUL_RAHMAN_MOSSAD_AL_ANKABUT_56_57 = Preset(
        r"Surahs\Abdul Rahman Mossad\Al-'Ankabut (29.53-64)",
        (56, 57),
        time_modifiers=TimeModifiers(time_modifier=-0.2, end_time_modifier=-0.5),
        additional_video_settings=AdditionalVideoSettings(end_line=12),
    )
    ABDUL_RAHMAN_MOSSAD_AL_GHASHIYAH_1_9 = Preset(
        r"Surahs\Abdul Rahman Mossad\Al-Ghashiyah (88.1-26)",
        (1, 9),
        time_modifiers=TimeModifiers(time_modifier=-0.2, end_time_modifier=-0.4),
    )
    ABDUL_RAHMAN_MOSSAD_AL_GHASHIYAH_10_26 = Preset(
        r"Surahs\Abdul Rahman Mossad\Al-Ghashiyah (88.1-26)",
        (10, 26),
    )
    ABDUL_RAHMAN_MOSSAD_AL_GHASHIYAH_10_16 = Preset(
        r"Surahs\Abdul Rahman Mossad\Al-Ghashiyah (88.1-26)",
        (10, 16),
        time_modifiers=TimeModifiers(time_modifier=-0.2, end_time_modifier=-0.6),
    )
    ABDUL_RAHMAN_MOSSAD_AL_GHASHIYAH_10_12 = Preset(
        r"Surahs\Abdul Rahman Mossad\Al-Ghashiyah (88.1-26)",
        (10, 12),
        time_modifiers=TimeModifiers(time_modifier=-0.2, end_time_modifier=-0.2),
    )
    ABDUL_RAHMAN_MOSSAD_AL_MAUN_1_7 = Preset(
        r"Surahs\Abdul Rahman Mossad\Al-Ma'un (107.1-7)",
        (1, 7),
    )
    ABDUL_RAHMAN_MOSSAD_AL_MUZZAMMIL_6_13 = Preset(
        r"Surahs\Abdul Rahman Mossad\Al-Muzzammil (73.1-20)",
        (6, 13),
        time_modifiers=TimeModifiers(time_modifier=-0.2, end_time_modifier=-0.3),
    )
    ABDUL_RAHMAN_MOSSAD_AL_MUZZAMMIL_14_18 = Preset(
        r"Surahs\Abdul Rahman Mossad\Al-Muzzammil (73.1-20)",
        (14, 18),
        time_modifiers=TimeModifiers(time_modifier=-0.2, end_time_modifier=-0.2),
    )
    ABDUL_RAHMAN_MOSSAD_AL_MUZZAMMIL_14_15 = Preset(
        r"Surahs\Abdul Rahman Mossad\Al-Muzzammil (73.1-20)",
        (14, 15),
        time_modifiers=TimeModifiers(time_modifier=-0.2, end_time_modifier=-0.2),
        additional_video_settings=AdditionalVideoSettings(end_line=28),
    )
    ABDUL_RAHMAN_MOSSAD_MARYAM_93_98 = Preset(
        r"Surahs\Abdul Rahman Mossad\Maryam (19.65-98)",
        (93, 98),
    )
    ABDUL_RAHMAN_MOSSAD_MARYAM_93_94 = Preset(
        r"Surahs\Abdul Rahman Mossad\Maryam (19.65-98)",
        (93, 94),
        time_modifiers=TimeModifiers(time_modifier=-0.2, end_time_modifier=-0.2),
    )
    ABDUL_RAHMAN_MOSSAD_YUNUS_7_10 = Preset(
        r"Surahs\Abdul Rahman Mossad\Yunus (10.3-25)",
        (7, 10),
        time_modifiers=TimeModifiers(time_modifier=-0.2, end_time_modifier=-0.2),
    )
    ABDUL_RAHMAN_MOSSAD_YUNUS_17_20 = Preset(
        r"Surahs\Abdul Rahman Mossad\Yunus (10.3-25)",
        (17, 20),
        time_modifiers=TimeModifiers(time_modifier=-0.2, end_time_modifier=-0.2),
    )
    ABDUL_RAHMAN_MOSSAD_YUNUS_17 = Preset(
        r"Surahs\Abdul Rahman Mossad\Yunus (10.3-25)",
        (17),
        time_modifiers=TimeModifiers(time_modifier=-0.2, end_time_modifier=-0.5),
    )
    ABDULLAH_AL_QARNI_MAIDAH_73_74 = Preset(
        r"Surahs\Abdullah Al-Qarni\Al-Ma'idah (5.72-76)",
        (73, 74),
        time_modifiers=TimeModifiers(time_modifier=-0.2, end_time_modifier=-0.2),
    )
    AHMED_KHEDR_TAHA_14_16 = Preset(
        r"Surahs\Ahmed Khedr\Taha (20.1-135)",
        (14, 16),
    )
    AHMED_WAEL_AL_AHZAB_56 = Preset(
        r"Surahs\Ahmed Wael\Al-Ahzab (33.56)",
        (56),
    )
    AHMED_WAEL_AS_SAFFAT_91_93 = Preset(
        r"Surahs\Ahmed Wael\As-Saffat (37.91-93)",
        (91, 93),
    )
    BANDAR_BALILAH_AL_ANAM_61_62 = Preset(
        r"Surahs\Bandar Balilah\Al-An'am (6.61-62)",
        (61, 62),
    )
    FAHAD_AL_KANDARI_AZ_ZALZALAH_1_8 = Preset(
        r"Surahs\Fahad Al-Kandari\Az-Zalzalah (99.1-8)",
        (1, 8),
    )
    FATIH_SEFERAGIC_AL_ALA = Preset(
        r"Surahs\Fatih Seferagic\Al-A'la (87.1-19)",
        (1, 19),
    )
    FATIH_SEFERAGIC_AL_BAQARAH_255 = Preset(
        r"Surahs\Fatih Seferagic\Al-Baqarah (2.255)",
        (255),
    )
    FATIH_SEFERAGIC_AL_HADID_20 = Preset(
        r"Surahs\Fatih Seferagic\Al-Hadid (57.20)",
        (20),
    )
    FATIH_SEFERAGIC_AL_HASHR_21_24 = Preset(
        r"Surahs\Fatih Seferagic\Al-Hashr (59.21-24)",
        (21, 24),
    )
    FATIH_SEFERAGIC_AL_HUJURAT_10_11 = Preset(
        r"Surahs\Fatih Seferagic\Al-Hujurat (49.10-11)",
        (10, 11),
    )
    FATIH_SEFERAGIC_AL_HUJURAT_10 = Preset(
        r"Surahs\Fatih Seferagic\Al-Hujurat (49.10-11)",
        (10),
        time_modifiers=TimeModifiers(time_modifier=-0.2, end_time_modifier=-0.4),
    )
    FATIH_SEFERAGIC_AL_MULK_1_5 = Preset(
        r"Surahs\Fatih Seferagic\Al-Mulk (67.1-30)",
        (1, 5),
        time_modifiers=TimeModifiers(time_modifier=-0.2, end_time_modifier=-0.3),
    )
    FATIH_SEFERAGIC_AL_MULK_6_11 = Preset(
        r"Surahs\Fatih Seferagic\Al-Mulk (67.1-30)",
        (6, 11),
        time_modifiers=TimeModifiers(time_modifier=-0.2, end_time_modifier=-0.4),
    )
    FATIH_SEFERAGIC_AL_MULK_12_18 = Preset(
        r"Surahs\Fatih Seferagic\Al-Mulk (67.1-30)",
        (12, 18),
    )
    FATIH_SEFERAGIC_AL_MULK_19_22 = Preset(
        r"Surahs\Fatih Seferagic\Al-Mulk (67.1-30)",
        (19, 22),
        time_modifiers=TimeModifiers(time_modifier=-0.2, end_time_modifier=-0.5),
    )
    FATIH_SEFERAGIC_AL_MULK_23_30 = Preset(
        r"Surahs\Fatih Seferagic\Al-Mulk (67.1-30)",
        (23, 30),
    )
    FATIH_SEFERAGIC_AL_QIYAMAH_1_12 = Preset(
        r"Surahs\Fatih Seferagic\Al-Qiyamah (75.1-40)",
        (1, 12),
        time_modifiers=TimeModifiers(time_modifier=-0.2, end_time_modifier=-0.4),
    )
    FATIH_SEFERAGIC_AL_QIYAMAH_13_19 = Preset(
        r"Surahs\Fatih Seferagic\Al-Qiyamah (75.1-40)",
        (13, 19),
        time_modifiers=TimeModifiers(time_modifier=-0.2, end_time_modifier=-0.4),
    )
    FATIH_SEFERAGIC_AN_NABA_1_16 = Preset(
        r"Surahs\Fatih Seferagic\An-Naba (78.1-40)",
        (1, 16),
        time_modifiers=TimeModifiers(time_modifier=-0.2, end_time_modifier=-0.4),
    )
    FATIH_SEFERAGIC_AN_NABA_17_30 = Preset(
        r"Surahs\Fatih Seferagic\An-Naba (78.1-40)",
        (17, 30),
        time_modifiers=TimeModifiers(time_modifier=-0.2, end_time_modifier=-1.3),
    )
    FATIH_SEFERAGIC_AN_NABA_31_40 = Preset(
        r"Surahs\Fatih Seferagic\An-Naba (78.1-40)",
        (31, 40),
    )
    FATIH_SEFERAGIC_AN_NISA_155_160 = Preset(
        r"Surahs\Fatih Seferagic\An-Nisa (4.155-160)",
        (155, 160),
    )
    FATIH_SEFERAGIC_AN_NUR_35 = Preset(
        r"Surahs\Fatih Seferagic\An-Nur (24.35)",
        (35),
    )
    FATIH_SEFERAGIC_AN_NUR_35_WITH_VIDEO = Preset(
        r"Surahs\Fatih Seferagic\An-Nur (24.35)",
        (35),
        additional_video_settings=AdditionalVideoSettings(
            single_background_video=r"Surahs\Fatih Seferagic\An-Nur (24.35)\video.mp4",
        ),
    )
    FATIH_SEFERAGIC_AR_RAHMAN_1_16 = Preset(
        r"Surahs\Fatih Seferagic\Ar-Rahman (55.1-16)",
        (1, 16),
    )
    FATIH_SEFERAGIC_AR_RAHMAN_35_39 = Preset(
        r"Surahs\Fatih Seferagic\Ar-Rahman (55.35-39)",
        (35, 39),
    )
    FATIH_SEFERAGIC_YA_SIN_77_83 = Preset(
        r"Surahs\Fatih Seferagic\Ya-Sin (36.77-83)",
        (77, 83),
    )
    IDRISS_ABKAR_AL_JINN_18_19 = Preset(
        r"Surahs\Idriss Abkar\Al-Jinn (72.18-19)",
        (18, 19),
    )
    IDRISS_ABKAR_AT_TUR_35_43 = Preset(
        r"Surahs\Idriss Abkar\At-Tur (52.35-43)",
        (35, 43),
    )
    ISLAM_SOBHI_YUSUF_86 = Preset(
        r"Surahs\Islam Sobhi\Yusuf (12.86)",
        (86),
    )
    ISLAM_SOBHI_AN_NAML_74_75 = Preset(
        r"Surahs\Islam Sobhi\An-Naml (27.66-93)",
        (74, 75),
        time_modifiers=TimeModifiers(time_modifier=-0.2, end_time_modifier=-0.6),
    )
    ISMAIL_ABOUD_AL_FURQAN_68_70 = Preset(
        r"Surahs\Ismail Aboud\Al-Furqan (25.68-70)",
        (68, 70),
    )
    MAHDI_ASH_SHISHANI_AL_KAFIRUN_1_6 = Preset(
        r"Surahs\Mahdi Ash-Shishani\Al-Kafirun (109.1-6)",
        (1, 6),
    )
    MANSOUR_AS_SALIMI_FURQAN_15 = Preset(
        r"Surahs\Mansour As Salimi\Al-Furqan (25.15)",
        (15),
    )
    MANSOUR_AS_SALIMI_MARYAM_27_33 = Preset(
        r"Surahs\Mansour As Salimi\Maryam (19.16-33)",
        (27, 33),
    )
    MANSOUR_AS_SALIMI_YUSUF_1_5 = Preset(
        r"Surahs\Mansour As Salimi\Yusuf (12.1-5)",
        (1, 5),
    )
    MOSTAFA_SHAIBANI_AL_QIYAMAH_20_27 = Preset(
        r"Surahs\Mostafa Shaibani\Al-Qiyamah (75.20-27)",
        (20, 27),
    )
    MUHAMMAD_AL_LUHAIDAN_ABASA_33_42 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\'Abasa (80.33-42)",
        (33, 42),
    )
    MUHAMMAD_AL_LUHAIDAN_AD_DUKHAN_43_49 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\Ad-Dukhan (44.43-49)",
        (43, 49),
    )
    MUHAMMAD_AL_LUHAIDAN_AL_AHQAF_30_31 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\Al-Ahqaf (46.30-31)",
        (30, 31),
    )
    MUHAMMAD_AL_LUHAIDAN_AL_AHZAB_63_66 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\Al-Ahzab (33.63-66)",
        (63, 66),
    )
    MUHAMMAD_AL_LUHAIDAN_AL_ANAM_27_30 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\Al-An'am (6.27-30)",
        (27, 30),
    )
    MUHAMMAD_AL_LUHAIDAN_AL_ANFAL_2 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\Al-Anfal (8.2-4)",
        (2),
        time_modifiers=TimeModifiers(time_modifier=-0.2, end_time_modifier=-0.2),
    )
    MUHAMMAD_AL_LUHAIDAN_AL_ANFAL_2_4 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\Al-Anfal (8.2-4)",
        (2, 4),
    )
    MUHAMMAD_AL_LUHAIDAN_AL_ARAF_40 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\Al-A'raf (7.1-206)",
        (40),
    )
    MUHAMMAD_AL_LUHAIDAN_AL_BAQARAH_138_141 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\Al-Baqarah (2.138-141)",
        (138, 141),
    )
    MUHAMMAD_AL_LUHAIDAN_AL_BAQARAH_214 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\Al-Baqarah (2.214)",
        (214),
    )
    MUHAMMAD_AL_LUHAIDAN_AL_BAQARAH_273_274 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\Al-Baqarah (2.273-274)",
        (273, 274),
    )
    MUHAMMAD_AL_LUHAIDAN_AL_BURUJ_12_22 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\Al-Buruj (85.12-22)",
        (12, 22),
    )
    MUHAMMAD_AL_LUHAIDAN_AL_FATH_22_23 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\Al-Fath (48.22-23)",
        (22, 23),
    )
    MUHAMMAD_AL_LUHAIDAN_AL_FURQAN_25_30 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\Al-Furqan (25.25-30)",
        (25, 30),
    )
    MUHAMMAD_AL_LUHAIDAN_AL_FURQAN_69_71 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\Al-Furqan (25.61-77)",
        (69, 71),
        time_modifiers=TimeModifiers(time_modifier=-0.2, end_time_modifier=-0.2),
    )
    MUHAMMAD_AL_LUHAIDAN_AL_FURQAN_69_77 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\Al-Furqan (25.61-77)",
        (69, 77),
    )
    MUHAMMAD_AL_LUHAIDAN_AL_FURQAN_71_77 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\Al-Furqan (25.61-77)",
        (71, 77),
    )
    MUHAMMAD_AL_LUHAIDAN_AL_FURQAN_72_77 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\Al-Furqan (25.61-77)",
        (72, 77),
    )
    MUHAMMAD_AL_LUHAIDAN_AL_FURQAN_74 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\Al-Furqan (25.61-77)",
        (74),
    )
    MUHAMMAD_AL_LUHAIDAN_AL_HAQQAH_29_33 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\Al-Haqqah (69.29-33)",
        (29, 33),
    )
    MUHAMMAD_AL_LUHAIDAN_ALI_IMRAN_15 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\Ali 'Imran (3.15)",
        (15),
    )
    MUHAMMAD_AL_LUHAIDAN_ALI_IMRAN_104_106 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\Ali 'Imran (3.104-106)",
        (104, 106),
    )
    MUHAMMAD_AL_LUHAIDAN_ALI_IMRAN_135_136 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\Ali 'Imran (3.135-136)",
        (135, 136),
    )
    MUHAMMAD_AL_LUHAIDAN_ALI_IMRAN_191_194 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\Ali 'Imran (3.191-194)",
        (191, 194),
    )
    MUHAMMAD_AL_LUHAIDAN_AL_INSAN_11_18 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\Al-Insan (76.11-22)",
        (11, 18),
        time_modifiers=TimeModifiers(time_modifier=-0.2, end_time_modifier=-0.3),
    )
    MUHAMMAD_AL_LUHAIDAN_AL_INSAN_19_22 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\Al-Insan (76.11-22)",
        (19, 22),
    )
    MUHAMMAD_AL_LUHAIDAN_AL_JATHIYAH_7_10 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\Al-Jathiyah (45.7-10)",
        (7, 10),
    )
    MUHAMMAD_AL_LUHAIDAN_AL_JATHIYAH_27_30 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\Al-Jathiyah (45.27-30)",
        (27, 30),
    )
    MUHAMMAD_AL_LUHAIDAN_AL_QAMAR_47_55 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\Al-Qamar (54.47-55)",
        (47, 55),
    )
    MUHAMMAD_AL_LUHAIDAN_AN_NAZIAT_34_41 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\An-Nazi'at (79.1-46)",
        (34, 41),
    )
    MUHAMMAD_AL_LUHAIDAN_AN_NISA_27_29 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\An-Nisa (4.27-29)",
        (27, 29),
    )
    MUHAMMAD_AL_LUHAIDAN_AN_NISA_27 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\An-Nisa (4.27-29)",
        (27),
        time_modifiers=TimeModifiers(time_modifier=-0.2, end_time_modifier=-0.4),
    )
    MUHAMMAD_AL_LUHAIDAN_AN_NISA_75_76 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\An-Nisa (4.75-76)",
        (75, 76),
    )
    MUHAMMAD_AL_LUHAIDAN_AN_NISA_122_123 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\An-Nisa (4.122-123)",
        (122, 123),
    )
    MUHAMMAD_AL_LUHAIDAN_AR_RAD_33_35 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\Ar-Ra'd (13.33-35)",
        (33, 35),
    )
    MUHAMMAD_AL_LUHAIDAN_AR_RAHMAN_40_47 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\Ar-Rahman (55.40-47)",
        (40, 47),
    )
    MUHAMMAD_AL_LUHAIDAN_AS_SAJDAH_12_14 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\As-Sajdah (32.12-14)",
        (12, 14),
    )
    MUHAMMAD_AL_LUHAIDAN_AZ_ZUMAR_22_23 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\Az-Zumar (39.22-23)",
        (22, 23),
    )
    MUHAMMAD_AL_LUHAIDAN_GHAFIR_48_52 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\Ghafir (40.48-52)",
        (48, 52),
    )
    MUHAMMAD_AL_LUHAIDAN_MARYAM_59_63 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\Maryam (19.59-63)",
        (59, 63),
    )
    MUHAMMAD_AL_LUHAIDAN_MARYAM_85_92 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\Maryam (19.85-92)",
        (85, 92),
    )
    MUHAMMAD_AL_LUHAIDAN_QAF_29_30 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\Qaf (50.29-30)",
        (29, 30),
    )
    MUHAMMAD_AL_LUHAIDAN_TAHA_105_108 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\Taha (20.105-108)",
        (105, 108),
    )
    MUHAMMAD_AL_LUHAIDAN_YA_SIN_51_58 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\Ya-Sin (36.51-58)",
        (51, 58),
    )
    MUHAMMAD_AL_LUHAIDAN_YA_SIN_59_62 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\Ya-Sin (36.59-62)",
        (59, 62),
    )
    MUHAMMAD_DIBIROV_IBRAHIM_12 = Preset(
        r"Surahs\Muhammad Dibirov\Ibrahim (14.12)",
        (12),
    )
    MUHAMMAD_DIBIROV_IBRAHIM_12_WITH_VIDEO = Preset(
        r"Surahs\Muhammad Dibirov\Ibrahim (14.12)",
        (12),
        additional_video_settings=AdditionalVideoSettings(
            single_background_video=r"Surahs\Muhammad Dibirov\Ibrahim (14.12)\video.mp4",
        ),
    )
    MUHAMMAD_DIBIROV_MARYAM_1_4 = Preset(
        r"Surahs\Muhammad Dibirov\Maryam (19.1-4)",
        (1, 4),
    )
    MUHAMMADLOIQ_QORI_AL_AHZAB_35 = Preset(
        r"Surahs\Muhammadloiq Qori\Al-Ahzab (33.35)",
        (35),
    )
    MUHAMMADLOIQ_QORI_AL_AHZAB_35_WITH_VIDEO = Preset(
        r"Surahs\Muhammadloiq Qori\Al-Ahzab (33.35)",
        (35),
        additional_video_settings=AdditionalVideoSettings(
            single_background_video=r"Surahs\Muhammadloiq Qori\Al-Ahzab (33.35)\video.mp4",
            single_background_video_horizontal_offset=400,
        ),
    )
    OBAIDA_MUAFAQ_GHAFIR_26_27 = Preset(
        r"Surahs\Obaida Muafaq\Ghafir (40.26-27)",
        (26, 27),
    )
    OBAIDA_MUAFAQ_GHAFIR_26_27_WITH_VIDEO = Preset(
        r"Surahs\Obaida Muafaq\Ghafir (40.26-27)",
        (26, 27),
        additional_video_settings=AdditionalVideoSettings(
            single_background_video=r"Surahs\Obaida Muafaq\Ghafir (40.26-27)\video.mp4",
        ),
    )
    OMAR_BN_DIAAALDEEN_AL_FURQAN_58 = Preset(
        r"Surahs\Omar Bn DiaaAldeen\Al-Furqan (25.58)",
        (58),
    )
    SALIM_BAHANAN_AD_DUHAA_1_11 = Preset(
        r"Surahs\Salim Bahanan\Ad-Duhaa (93.1-11)",
        (1, 11),
    )
    SALIM_BAHANAN_AL_FATIHAH_2_7 = Preset(
        r"Surahs\Salim Bahanan\Al-Fatihah (1.1-7)",
        (2, 7),
    )
    SALIM_BAHANAN_AL_QARIAH_1_11 = Preset(
        r"Surahs\Salim Bahanan\Al-Qari'ah (101.1-11)",
        (1, 11),
    )
    SALIM_BAHANAN_AT_TIN_1_8 = Preset(
        r"Surahs\Salim Bahanan\At-Tin (95.1-8)",
        (1, 8),
    )
    UMAIR_SHAMIM_AL_HIJR_30_35 = Preset(
        r"Surahs\Umair Shamim\Al-Hijr (15.30-35)",
        (30, 35),
    )
    UMAIR_SHAMIM_AS_SAFFAT_149_163 = Preset(
        r"Surahs\Umair Shamim\As-Saffat (37.149-163)",
        (149, 163),
    )
    UMAR_SILDINSKIY_AL_INFITAR_9_19 = Preset(
        r"Surahs\Umar Sildinskiy\Al-Infitar (82.9-19)",
        (9, 19),
    )
    UNKNOWN_ADH_DHARIYAT_17_28 = Preset(
        r"Surahs\Unknown\Adh-Dhariyat (51.17-28)",
        (17, 28),
    )
    UNKNOWN_AL_ANKABUT_56_58 = Preset(
        r"Surahs\Unknown\Al-'Ankabut (29.56-58)",
        (56, 58),
    )
    UNKNOWN_AL_ANKABUT_56_57 = Preset(
        r"Surahs\Unknown\Al-'Ankabut (29.56-58)",
        (56, 57),
        time_modifiers=TimeModifiers(time_modifier=-0.2, end_time_modifier=-0.2),
    )
    UNKNOWN_AL_BAQARAH_153_157 = Preset(
        r"Surahs\Unknown\Al-Baqarah (2.153-157)",
        (153, 157),
    )
    UNKNOWN_AL_BAQARAH_285 = Preset(
        r"Surahs\Unknown\Al-Baqarah (2.285)",
        (285),
    )
    UNKNOWN_AL_FURQAN_63_70 = Preset(
        r"Surahs\Unknown\Al-Furqan (25.63-70)",
        (63, 70),
    )
    UNKNOWN_AL_FURQAN_72_75 = Preset(
        r"Surahs\Unknown\Al-Furqan (25.72-75)",
        (72, 75),
    )
    UNKNOWN_AL_HUJURAT_12 = Preset(
        r"Surahs\Unknown\Al-Hujurat (49.12)",
        (12),
    )
    UNKNOWN_AL_KAHF_46 = Preset(
        r"Surahs\Unknown\Al-Kahf (18.46)",
        (46),
    )
    UNKNOWN_AL_MUMINUN_1_6 = Preset(
        r"Surahs\Unknown\Al-Mu'minun (23.1-6)",
        (1, 6),
    )
    UNKNOWN_AN_NASR_1_3 = Preset(
        r"Surahs\Unknown\An-Nasr (110.1-3)",
        (1, 3),
    )
    UNKNOWN_AS_SAFFAT_123_132 = Preset(
        r"Surahs\Unknown\As-Saffat (37.123-132)",
        (123, 132),
    )
    UNKNOWN_AZ_ZUMAR_71_75 = Preset(
        r"Surahs\Unknown\Az-Zumar (39.71-75)",
        (71, 75),
    )
    UNKNOWN_AZ_ZUMAR_71_75_WITH_VIDEO = Preset(
        r"Surahs\Unknown\Az-Zumar (39.71-75)",
        (71, 75),
        additional_video_settings=AdditionalVideoSettings(
            single_background_video=r"Surahs\Unknown\Az-Zumar (39.71-75)\video.mp4",
            single_background_video_horizontal_offset=700,
        ),
    )
    UNKNOWN_AZ_ZUMAR_73_75 = Preset(
        r"Surahs\Unknown\Az-Zumar (39.71-75)",
        (73, 75),
    )
    UNKNOWN_AZ_ZUMAR_73_75_WITH_VIDEO = Preset(
        r"Surahs\Unknown\Az-Zumar (39.71-75)",
        (73, 75),
        additional_video_settings=AdditionalVideoSettings(
            single_background_video=r"Surahs\Unknown\Az-Zumar (39.71-75)\video.mp4",
        ),
    )
    UNKNOWN_TAHA_124_126 = Preset(
        r"Surahs\Unknown\Taha (20.124-126)",
        (124, 126),
    )
    YASSER_AL_DOSARI_AL_FATH_29 = Preset(
        r"Surahs\Yasser Al-Dosari\Al-Fath (48.29)",
        (29),
    )
    YASSER_AL_DOSARI_ALI_IMRAN_162_163 = Preset(
        r"Surahs\Yasser Al-Dosari\Ali 'Imran (3.162-163)",
        (162, 163),
    )
    YASSER_AL_DOSARI_AL_ISRA_9_12 = Preset(
        r"Surahs\Yasser Al-Dosari\Al-Isra (17.9-12)",
        (9, 12),
    )
    YASSER_AL_DOSARI_AL_MAIDAH_114_115 = Preset(
        r"Surahs\Yasser Al-Dosari\Al-Ma'idah (5.114-115)",
        (114, 115),
    )
    YASSER_AL_DOSARI_AL_MUMINUN_34_39 = Preset(
        r"Surahs\Yasser Al-Dosari\Al-Mu'minun (23.34-39)",
        (34, 39),
    )
    YASSER_AL_DOSARI_AL_MUMINUN_84_92 = Preset(
        r"Surahs\Yasser Al-Dosari\Al-Mu'minun (23.84-92)",
        (84, 92),
    )
    YASSER_AL_DOSARI_AL_MUTAFFIFIN_18_28 = Preset(
        r"Surahs\Yasser Al-Dosari\Al-Mutaffifin (83.18-28)",
        (18, 28),
    )
    YASSER_AL_DOSARI_AL_QASAS_7_8 = Preset(
        r"Surahs\Yasser Al-Dosari\Al-Qasas (28.7-8)",
        (7, 8),
    )
    YASSER_AL_DOSARI_AL_QASAS_32_34 = Preset(
        r"Surahs\Yasser Al-Dosari\Al-Qasas (28.32-34)",
        (32, 34),
    )
    YASSER_AL_DOSARI_AR_RAHMAN_17_25 = Preset(
        r"Surahs\Yasser Al-Dosari\Ar-Rahman (55.1-78)",
        (17, 25),
        time_modifiers=TimeModifiers(time_modifier=-0.2, end_time_modifier=-0.4),
    )
    YASSER_AL_DOSARI_AR_RAHMAN_26_34 = Preset(
        r"Surahs\Yasser Al-Dosari\Ar-Rahman (55.1-78)",
        (26, 34),
        time_modifiers=TimeModifiers(time_modifier=-0.2, end_time_modifier=-0.3),
    )
    YASSER_AL_DOSARI_ASH_SHARH_1_8 = Preset(
        r"Surahs\Yasser Al-Dosari\Ash-Sharh (94.1-8)",
        (1, 8),
    )
    YASSER_AL_DOSARI_AZ_ZUKHRUF_68_73 = Preset(
        r"Surahs\Yasser Al-Dosari\Az-Zukhruf (43.68-80)",
        (68, 73),
        time_modifiers=TimeModifiers(time_modifier=-0.2, end_time_modifier=-0.4),
    )
    YASSER_AL_DOSARI_AZ_ZUKHRUF_74_80 = Preset(
        r"Surahs\Yasser Al-Dosari\Az-Zukhruf (43.68-80)",
        (74, 80),
    )
    YASSER_AL_DOSARI_LUQMAN_8_11 = Preset(
        r"Surahs\Yasser Al-Dosari\Luqman (31.8-11)",
        (8, 11),
    )
    YOUSEF_AL_SOQIER_ASH_SHUARA_87_95 = Preset(
        r"Surahs\Yousef Al-Soqier\Ash-Shu'ara (26.87-95)",
        (87, 95),
    )
    YOUSEF_AL_SOQIER_QAF_19_22 = Preset(
        r"Surahs\Yousef Al-Soqier\Qaf (50.19-22)",
        (19, 22),
    )
    YOUSEF_AL_SOQIER_YA_SIN_63_65 = Preset(
        r"Surahs\Yousef Al-Soqier\Ya-Sin (36.55-67)",
        (63, 65),
        time_modifiers=TimeModifiers(time_modifier=-0.2, end_time_modifier=-0.2),
    )
    YOUSEF_AL_SOQIER_YA_SIN_63_65_WITH_VIDEO = Preset(
        r"Surahs\Yousef Al-Soqier\Ya-Sin (36.55-67)",
        (63, 65),
        time_modifiers=TimeModifiers(time_modifier=-0.2, end_time_modifier=-0.4),
        additional_video_settings=AdditionalVideoSettings(
            single_background_video=r"Surahs\Yousef Al-Soqier\Ya-Sin (36.55-67)\video.mp4",
            single_background_video_horizontal_offset=300,
        ),
    )
    ############################################################################################################################################################
    ############################################################################################################################################################
    ############################################################################################################################################################
    ############################################################################################################################################################
    ############################################################################################################################################################
    MUHAMMAD_AL_LUHAIDAN_AL_AHZAB_23_24 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\Al-Ahzab (33.23-24)",
        (23, 24),
    )
    MUHAMMAD_AL_LUHAIDAN_ALI_IMRAN_16_17 = Preset(
        r"Surahs\Muhammad Al-Luhaidan\Ali 'Imran (3.16-17)",
        (16, 17),
    )
