from django.urls import path
from django.views.generic import TemplateView
from django.shortcuts import render
from django.views.generic import TemplateView
from . import views

# создаем класс для добавления страниц без view
class ModelNameTemplateView(TemplateView):
    template_name = None

urlpatterns = [
    #path("", views.index, name="index"),
    #path('base/', views.empty_view_base(), name='base'),
    #path('child/', views.empty_view_child, name='child'),
    path('', ModelNameTemplateView.as_view(template_name='base.html'), name='base'),
    path('child/', ModelNameTemplateView.as_view(template_name='child.html'), name='child'),
    path('main/', ModelNameTemplateView.as_view(template_name='temp2/main.html'), name='main'),
    path('page1', ModelNameTemplateView.as_view(template_name='temp2/page1.html'), name='page1'),
    path('page2', ModelNameTemplateView.as_view(template_name='temp2/page2.html'), name='page2'),
]