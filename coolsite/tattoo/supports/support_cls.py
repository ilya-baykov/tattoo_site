class MainData:
    """ Класс хранит в себе информацию о title , header и описания страницы """
    PATH = r"C:\Users\ilyab\PycharmProjects\tattoo_site_1\coolsite\tattoo\supports\texts"

    def __init__(self, title="Tattoo", header="", link_text=""):
        self.__title = title
        self.__header = header
        self.__link_text = link_text

    @property
    def title(self):
        return self.__title

    @property
    def header(self):
        return self.__header

    @property
    def description(self):
        """ Принимает ссылку на файл и возвращеает его текст """
        current_path = MainData.PATH + f"\{self.__link_text}"
        with open(current_path, "r", encoding="utf-8") as main_text:
            content = main_text.read()
            return content

    def __str__(self):
        return f"Экземпляр класса {self.__title} {self.__header} "


class TattooStyle:
    __TATTOO_STYLE_DICT = {}

    def __init__(self, position: int, style_en: str, style_ru: str):
        self.__position = position
        self.__style_en = style_en
        self.__style_ru = style_ru
        TattooStyle.__TATTOO_STYLE_DICT.setdefault(position, []).extend([style_en, style_ru])

    @property
    def position(self):
        return self.__position

    @property
    def style_en(self):
        return self.__style_en

    @property
    def style_ru(self):
        return self.__style_ru

    @classmethod
    def tattoo_style_dict(cls):
        return cls.__TATTOO_STYLE_DICT

    def __str__(self):
        return f"({self.__position}, {self.__style_en}, {self.__style_ru}"



