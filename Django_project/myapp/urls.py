from django.urls import path, re_path
from myapp.views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', index, name='index'),
    path('article/', article, name='article'),
    path('article/archive/', article_archive, name='article_archive'),
    path('users/', users, name='users'),
    path('article/<int:article_number>/', article_detail, name='article_detail'),
    path('article/<int:article_number>/archive/', article_archive_number, name='article_archive_number'),
    path('article/<int:article_number>/<slug:slug_text>/', article_with_slug, name='article_with_slug'),
    path('users/<int:user_number>/', user_detail, name='user_detail'),
    re_path(r'^phone/(?P<phone_number>(050|067|063|093|096|098)[0-9]{7})/$', phone_detail, name='phone_detail'),
    re_path(r'^numbers_and_letters/(?P<new_param>[1-9a-f]{4}-[0-9a-f]{6})/$', numbers_and_letters,
            name='numbers_and_letters'),
    path('random_article_slug/', random_article_slug, name='random_article_slug'),
    path('random_article/', random_article, name='random_article'),
    path('article_with_num/<int:article_number>/<str:num_text>/', article_with_num, name='article_with_num'),
    path('authors/', authors_list, name='authors_list'),
    path('catalog/', catalog, name='catalog'),
    path('books/', books_catalog, name='books_catalog'),
    path('book_request/', book_request, name='book_request'),
    path('blog/', blog, name='blog'),
    path('art/', art_list, name='art_list'),
    path('like/<int:article_id>/', like_article, name='like_article'),
    path('add_reply/<int:comment_id>/', add_reply, name='add_reply'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('recruiter/', recruiter_form_view, name='recruiter'),
    path('success/', success, name='success'),
    path('login/', login_view, name='login'),
    path('logout/', logo, name='logout'),
    path('register/', register_view, name='register'),
    path('change_password/', change_password_view, name='change_password'),
    path('search-comments/', search_comments, name='search_comments'),

]

