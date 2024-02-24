import random
import string
from django.http import HttpResponse
from django.shortcuts import render, redirect
from myapp.models import Authors, Books, Book, ReaderInfo, Article, Comment
from myapp.forms import CommentForm
from django.contrib.auth.models import User
from .forms import RecruiterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def index(request):
    data = {'title': 'Home page my website'}
    return render(request, 'index.html', context=data)


def article(request):
    return render(request, 'article.html', {'text': 'Hello article.html'})


def article_archive(request):
    return render(request, 'article_archive.html', {'text': 'Watch this page'})


def users(request):
    return render(request, 'users.html', {'text': 'here file users.html'})


def article_detail(request, article_number):
    return render(request, 'article_detail.html', {'text': 'Hi Article_detail!', 'article_number': article_number})


def article_archive_number(request, article_number):
    return render(request, 'article_archive_number.html',
                  {'text': 'Your on the article_archive_number page'})


def article_with_slug(request, article_number, slug_text=None):
    context = {'article_number': article_number, 'slug_text': slug_text}
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


def authors_list(request):
    authors = Authors.objects.all()
    return render(request, 'authors_list.html', {'authors': authors})


def catalog(request):
    books = Books.objects.all()
    return render(request, 'books_list.html', {'books': books})


def books_catalog(request):
    books = Book.objects.all()
    return render(request, 'library.html', {'books': books})


def book_request(request):
    if request.method == 'POST':
        book_title = request.POST.get('book-title')
        reader_name = request.POST.get('username')
        is_available = request.POST.get('availability')

        if book_title and reader_name:
            try:
                book = Book.objects.get(title=book_title)
            except Book.DoesNotExist:
                return render(request, 'index.html')

            reader, created = ReaderInfo.objects.get_or_create(name=reader_name)
            book.reader = reader
            book.is_available = False if is_available == 'unavailable' else True
            book.save()
            book_request_info = f"Book '{book.title}' request processed successfully."
            return render(request, 'book_request.html', {'book_request_info': book_request_info,
                                                         'books': Book.objects.all(),
                                                         'reader': reader})

    return render(request, 'book_request.html')


def add_reply(request, comment_id):
    comment = Comment.objects.get(id=comment_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            artic = comment.article
            yura = User.objects.get(username='Yura')
            new_comment = Comment.objects.create(
                article=artic,
                parent_comment=comment,
                author=yura,
                content=form.cleaned_data['comment']
            )
            return render(request, 'add_reply.html', {'form': form, 'comment': comment, 'new_comment': new_comment})
    else:
        form = CommentForm()

    return render(request, 'add_reply.html', {'form': form, 'comment': comment})


def art_list(request):
    articles = Article.objects.all()
    return render(request, 'like.html', {'articles': articles})


def like_article(request, article_id):
    if request.method == 'POST':
        action = request.POST.get('action')
        article = Article.objects.get(pk=article_id)
        if action == 'like':
            article.likes += 1
        elif action == 'dislike':
            article.dislikes += 1
        article.save()
    return redirect('art_list')


def blog(request):
    articles = Article.objects.all()
    comments = Comment.objects.all()

    context = {
        'articles': articles,
        'comments': comments
    }

    return render(request, 'blog.html', context)


def recruiter_form_view(request):
    if request.method == 'POST':
        form = RecruiterForm(request.POST)
        if form.is_valid() and form.recruiter_validate():
            return redirect('success')
        else:
            messages.error(request, 'No form correct')
    else:
        form = RecruiterForm()

    return render(request, 'recruiter_form.html', {'form': form})


def success(request):
    return render(request, 'success_page.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            if User.objects.filter(username=username).exists():
                return render(request, 'login.html', {'error_message': 'Invalid password'})
            else:
                new_user = User.objects.create_user(username=username, password=password)
                login(request, new_user)
                return redirect('index')
    else:
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def register_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.save()
                return redirect('index')
            else:
                return render(request, 'register.html', {'error_message': 'there is already a user with the same name'})
        else:
            return render(request, 'register.html')
    else:
        return redirect('login')


def change_password_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')

        if new_password1 != new_password2:
            return render(request, 'change_password.html', {'error_message': 'Password mismatch'})

        user = authenticate(username=request.user.username, password=current_password)
        if user is not None:
            user.set_password(new_password1)
            user.save()
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'change_password.html', {'error_message': 'Incorrect password'})
    else:
        return render(request, 'change_password.html')


def search_comments(request):
    search_text = request.GET.get('search_text')
    my_comments = request.GET.get('my_comments')

    comments = Comment.objects.filter(content__icontains=search_text) if search_text else Comment.objects.all()

    if my_comments and request.user.is_authenticated:
        comments = comments.filter(author=request.user)

    context = {'comments': comments, 'search_text': search_text, 'my_comments': my_comments}
    return render(request, 'search_comments.html', context)