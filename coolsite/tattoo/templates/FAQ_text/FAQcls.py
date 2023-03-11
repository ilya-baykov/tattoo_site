class Faq:
    """
        Класс для реализации вывода информации с ответами на популярные вопросы.
        Принимает в себя один обязательный параметр по которому будет строиться ссылка на файл.
        А также один не обязательный, в котором будет сформулирован вопрос страницы.
        Возвращает текст файла с описанием (ответ на вопрос из FAQ)
    """
    __PATH = r"C:\Users\ilyab\PycharmProjects\tattoo_site_1\coolsite\tattoo\templates\FAQ_text"

    def __init__(self, name, header):
        self.__name = name
        self.__header = header

    @property
    def description(self):
        try:
            link_to_file = Faq.__PATH + '\\' + self.__name
            with open(link_to_file, "r", encoding="utf-8") as info:
                text = info.read()
                return text
        except FileNotFoundError:
            return "Что то пошло не так :c"

    @property
    def name(self):
        return self.__name

    @property
    def header(self):
        return self.__header

    def __str__(self):
        return self.__name


preparation = Faq("preparation", "Как мне подготовится к посещению тату салона?")
price = Faq("price", "Сколько будет стоить татуировка?")
tattoo_care = Faq("tattoo_care", "Как мне ухаживать за новой татуировкой?")
error_faq = Faq("error", "Нам жаль, но мы не нашли такой вопрос в нашей базе:c",)
