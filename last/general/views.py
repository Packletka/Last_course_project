from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return render(request, 'general/main.html')


def pattern(request):
    return render(request, 'general/pattern.html')
