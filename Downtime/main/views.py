# encoding=utf-8

from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def login(request):
    return render(request, "log-in.html")


def signup(request):
    return render(request, "sign-up.html")
