from django.shortcuts import render
from .supports import support_function as sf


# Create your views here.

def main_menu(request):
    contex = {
        "title_info": sf.main_menu_info.get("title_info"),  # Возвращает текст для <title>
        "header": sf.main_menu_info.get("header"),
        "description": sf.main_menu_info.get("description")  # Возвращает описание страницы
    }
    return render(request, "tattoo_main_info.html", context=contex)
