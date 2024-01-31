from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('articles/', articles),
    path('articles/archive/', article_archive),
    path('users/', users),
]