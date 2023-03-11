from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_menu),
    path('/history', views.history),
    path('/style', views.style_menu),
    path('/help', views.help_menu),
    path('/help/<str:question>', views.faq_question),
    path('/style/<int:current_style>', views.current_style_int),
    path('/style/<str:current_style>', views.current_style_fn, name="link_current_style"),
]
