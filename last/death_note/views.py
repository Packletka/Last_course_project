from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h2>Greetings!</h2>")


def about(request):
    return HttpResponse("<h1>About us</h1>")
