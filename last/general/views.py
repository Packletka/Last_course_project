from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'general/index.html')


def about(request):
    return render(request, 'general/about.html')


def sidebar(request):
    return render(request, 'general/sidebar.html')
