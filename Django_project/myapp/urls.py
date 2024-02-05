from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('article/', article, name='articles'),
    path('article/archive/', article_archive, name='article_archive'),
    path('users/', users, name='users'),
    path('article/<int:article_number>/', article_detail, name='article_detail'),
    path('article/<int:article_number>/archive/', article_archive_number, name='article_archive_number'),
    path('article/<int:article_number>/<slug:slug_text>/', article_with_slug, name='article_with_slug'),
    path('users/<int:user_number>/', user_detail, name='user_detail'),
    re_path(r'^phone/(?P<phone_number>0[5-9][0-9]{8})/$', phone_detail, name='phone_detail'),
    re_path(r'^numbers_and_letters/(?P<new_param>[1-9a-f]{4}-[0-9a-f]{6})/$', numbers_and_letters,
            name='numbers_and_letters'),
]

