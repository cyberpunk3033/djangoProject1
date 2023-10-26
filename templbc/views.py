from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def empty_view_base(request):
    return render(request, 'base.html')

def empty_view_child(request):
    return render(request, 'child.html')