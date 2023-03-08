PATH = r"C:\Users\ilyab\PycharmProjects\tattoo_site_1\coolsite\tattoo\supports\texts"


class MainData:
    """ Класс хранит в себе информацию о title , header и описания страницы """

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
        current_path = PATH + f"\{self.__link_text}"
        with open(current_path, "r", encoding="utf-8") as main_text:
            content = main_text.read()
            return content

    def __str__(self):
        return f"Экземпляр класса {self.__title} {self.__header} "


main_menu_info_cls = MainData("Tattoo", "Татуировка", "main_text")
history_info = MainData("History", "История", "history_text")
