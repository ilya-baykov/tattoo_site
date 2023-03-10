from django.shortcuts import render
from .supports import support_cls as sc
from .supports import instances_cls as inst
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
# translator = dict(zip([sc.TattooStyle.tattoo_style_en_list()], [sc.TattooStyle.tattoo_style_ru_list()]))


def main_menu(request):
    contex = {
        "title_info": inst.main_menu_info_cls.title,  # Возвращает текст для <title>
        "header": inst.main_menu_info_cls.header,  # Возвращает текст для <header>
        "description": inst.main_menu_info_cls.description  # Возвращает описание страницы
    }
    return render(request, "tattoo_main_info.html", context=contex)


def history(request):
    contex = {
        "title_info": inst.history_info.title,  # Возвращает текст для <title>
        "header": inst.history_info.header,  # Возвращает текст для <header>
        "description": inst.history_info.description  # Возвращает описание страницы
    }
    return render(request, "history.html", context=contex)


def style_menu(request):
    contex = {
        "style_list": sc.TattooStyle.tattoo_style_dict()  # Возвращает словарь со всеми стилями
    }
    return render(request, "style_menu.html", context=contex)


def current_style_fn(request, current_style: str):
    info = sc.TattooStyle.get_info(current_style)
    if isinstance(info, str):
        return render(request, "ex_current_style.html", context={"exception_description": info})
    contex = {
        "availability_check": True,
        "current_style_en": current_style,
        "header": info[1],
        "description": info[2],
        "position": info[3]
    }
    return render(request, "current_style_info.html", context=contex)


def current_style_int(request, current_style: int):
    counter_style = sc.TattooStyle.tattoo_style_counter()
    if counter_style >= current_style > 0:
        style_position = sc.TattooStyle.tattoo_style_en_list()[current_style - 1]
        return HttpResponseRedirect(f"/tattoo/style/{style_position}")
    return render(request, "ex_current_style.html",
                  context={"exception_description": f"Стиль под номером {current_style} не найден"})
