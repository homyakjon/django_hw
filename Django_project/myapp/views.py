import random
import string
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return render(request, 'index.html', {'content': 'Information about index.html'})


def article(request):
    return render(request, 'article.html', {'content': 'Hello article.html'})


def article_archive(request):
    return render(request, 'article_archive.html', {'content': 'Watch this page'})


def users(request):
    return render(request, 'users.html', {'content': 'here file users.html'})


def article_detail(request, article_number):
    return render(request, 'article_detail.html', {'content': 'Hi Article_detail!', 'article_number': article_number})


def article_archive_number(request, article_number):
    return render(request, 'article_archive_number.html',
                  {'content': 'Your on the article_archive_number page'})


def article_with_slug(request, article_number, slug_text=None):
    home_page_url = reverse('index')
    context = {'article_number': article_number, 'slug_text': slug_text, 'home_page_url': home_page_url}
    if slug_text:
        return render(request, 'slug_content.html', context)
    return render(request, 'article_with_slug.html', context)


def article_with_num(request, article_number, num_text):
    context = {
        'article_number': article_number,
        'num_text': num_text,
    }
    return render(request, 'num_content.html', context)


def user_detail(request, user_number):
    return HttpResponse(f"<h2>User Detail</h2>: {user_number}")


def phone_detail(request, phone_number):
    return HttpResponse(f"<h2>Phone number</h2>: {phone_number}")


def numbers_and_letters(request, new_param):
    return HttpResponse(f"New parameter: {new_param}")


def random_article_slug(request):
    random_article_id = random.randint(1, 10)
    random_slug = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(5, 10)))
    return redirect('article_with_slug', article_number=random_article_id, slug_text=random_slug)


def random_article(request):
    random_article_id = random.randint(1, 10)
    number = ''.join(random.choice(string.digits))
    return redirect('article_with_num', article_number=random_article_id, num_text=number)