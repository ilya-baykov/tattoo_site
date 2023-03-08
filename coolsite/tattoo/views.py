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


def style_menu(request):
    contex = {
        "style_list": sc.TATTOO_STYLE_DICT  # Возвращает список всех стилей
    }
    return render(request, "style_menu.html", context=contex)


def current_style_fn(request, current_style):
    contex = {
        "availability_check": current_style in sc.TATTOO_STYLE_DICT.values(),
        "current_style": current_style
    }
    return render(request, "current_style_info.html", context=contex)
