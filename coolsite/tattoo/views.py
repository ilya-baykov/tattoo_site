from django.shortcuts import render
from .supports import support_cls as sc
from .supports import instances_cls as inst


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


def current_style_fn(request, current_style):
    info = sc.TattooStyle.get_info(current_style)
    if isinstance(info, str):
        contex = {
            "exception_description": info
        }
        return render(request, "ex_current_style.html", context=contex)
    contex = {
        "availability_check": True,
        "current_style_en": current_style,
        "header": info[1],
        "description": info[2],
        "position": info[3]
    }
    return render(request, "current_style_info.html", context=contex)
# def current_style_fn(request, current_style):
#     if sc.TattooStyle.availability_check(current_style):
#         info = sc.TattooStyle.get_info(current_style)
#         header = info[1]
#     else:
#         header = ""
#         info = ["", "", "", ""]
#     contex = {
#         "availability_check": True,
#         "current_style_en": current_style,
#         "header": header,
#         "description": info[2],
#         "position": info[3]
#     }
#     return render(request, "current_style_info.html", context=contex)
