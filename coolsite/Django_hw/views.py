from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("<h1>Страница приложения rock_groups</h1>")


def articles(request):
    return HttpResponse("<h1>articles.html</h1>")


def article_archive(request):
    return HttpResponse("<h1>article_archive.html</h1>")


def users(request):
    return HttpResponse("<h1>users.html</h1>")