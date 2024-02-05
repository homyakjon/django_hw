from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("<h1>Страница приложения rock_groups</h1>")


def article(request):
    return HttpResponse("<h1>articles.html</h1>")


def article_archive(request):
    return HttpResponse("<h1>article_archive.html</h1>")


def users(request):
    return HttpResponse("<h1>users.html</h1>")


def article_detail(request, article_number):
    return HttpResponse(f"<h1>Article Detail<h1/>: {article_number}")


def article_archive_number(request, article_number):
    return HttpResponse(f"<h1>Article Archive</h1>: {article_number}")


def article_with_slug(request, article_number, slug_text):
    return HttpResponse(f"<h1>Article with Slug</h1>: {article_number}, {slug_text}")


def user_detail(request, user_number):
    return HttpResponse(f"<h2>User Detail</h2>: {user_number}")


def phone_detail(request, phone_number):
    return HttpResponse(f"<h2>Phone number</h2>: {phone_number}")


def numbers_and_letters(request, new_param):
    return HttpResponse(f"New parameter: {new_param}")
