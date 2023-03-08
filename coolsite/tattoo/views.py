from django.shortcuts import render
from .supports import support_cls as sc


# Create your views here.
def main_menu(request):
    contex = {
        "title_info": sc.main_menu_info_cls.title,  # Возвращает текст для <title>
        "header": sc.main_menu_info_cls.header,  # Возвращает текст для <header>
        "description": sc.main_menu_info_cls.description  # Возвращает описание страницы
    }
    return render(request, "tattoo_main_info.html", context=contex)


def history(request):
    contex = {
        "title_info": sc.history_info.title,  # Возвращает текст для <title>
        "header": sc.history_info.header,  # Возвращает текст для <header>
        "description": sc.history_info.description  # Возвращает описание страницы
    }
    return render(request, "history.html", context=contex)
