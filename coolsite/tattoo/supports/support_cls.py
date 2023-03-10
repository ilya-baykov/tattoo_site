class MainData:
    """ Класс хранит в себе информацию о title , header и описания страницы """
    __PATH = r"C:\Users\ilyab\PycharmProjects\tattoo_site_1\coolsite\tattoo\supports\texts"

    def __init__(self, title="Tattoo", header="", link_text=""):
        self.__title = title
        self.__header = header
        self.__link_text = link_text

    @property
    def title(self) -> str:
        return self.__title

    @property
    def header(self) -> str:
        return self.__header

    @property
    def description(self) -> str:
        """ Принимает ссылку на файл и возвращеает его текст """
        current_path = MainData.__PATH + f"\{self.__link_text}"
        try:
            with open(current_path, "r", encoding="utf-8") as main_text:
                content = main_text.read()
                return content
        except Exception:
            return ":c"

    def __str__(self) -> str:
        return f"Экземпляр класса {self.__title} {self.__header} "


########################################################################################################################
class TattooStyle:
    __TATTOO_STYLE_DICT = {}
    __PATH = r"C:\Users\ilyab\PycharmProjects\tattoo_site_1\coolsite\tattoo\templates\styles_info"

    def __init__(self, position: int, style_en: str, style_ru: str, link_text="OldSchool"):
        self.__position = position
        self.__style_en = style_en
        self.__style_ru = style_ru
        self.__link_text = link_text
        TattooStyle.__TATTOO_STYLE_DICT.setdefault(self.__style_en.lower(), []).extend(
            [style_en, style_ru, TattooStyle.description(self), position])

    def description(self) -> str:
        """ Принимает ссылку на файл и возвращеает его текст """
        current_path = TattooStyle.__PATH + f"\{self.__link_text}"
        try:
            with open(current_path, "r", encoding="utf-8") as style_text:
                content = style_text.read()
                return content
        except Exception:
            return ":c"

    @classmethod
    def tattoo_style_dict(cls) -> dict:
        """Возвращает словарь с иноформацией о всех стилях """
        return cls.__TATTOO_STYLE_DICT

    @classmethod
    def tattoo_style_ru_list(cls) -> list:
        """
        ['oldschool', 'newschool', 'realism', 'biomechanics', 'graphic', 'japanese', 'blackwork', 'lettering', 'chicano', 'ornamental']
        """
        return [stl[1].lower() for stl in TattooStyle.__TATTOO_STYLE_DICT.values()]

    @classmethod
    def tattoo_style_en_list(cls) -> list:
        """
        ['традиционный стиль (олд скул)', 'нью скул', 'реализм', 'биомеханика', 'графика', 'японские татуировки', 'блэкворк', 'леттеринг', 'чикано', 'орнаментал']
        """
        return [stl[0].lower() for stl in TattooStyle.__TATTOO_STYLE_DICT.values()]

    @classmethod
    def availability_check(cls, style: str):
        """ Проверяет наличие style  в списке всех стилей """
        return style.lower() in cls.tattoo_style_en_list()

    @classmethod
    def get_info(cls, style) -> list | str:
        if TattooStyle.availability_check(style):
            return cls.tattoo_style_dict().get(style.lower())
        else:
            return f"Мы не знаем такой стиль  - {style}"

    def __str__(self) -> str:
        return f"({self.__position}, {self.__style_en}, {self.__style_ru}"
