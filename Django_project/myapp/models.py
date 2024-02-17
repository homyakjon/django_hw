from datetime import timedelta

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation


class MyApp(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Authors(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Books(models.Model):
    title = models.CharField(max_length=150)
    authors = models.ForeignKey(Authors, on_delete=models.CASCADE)
    reader = models.CharField(max_length=100, null=True, blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=150)
    authors = models.ManyToManyField(Author)
    reader = models.ForeignKey('ReaderInfo', on_delete=models.SET_NULL, null=True, blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class ReaderInfo(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def get_title(self):
        return str(self.title)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return f"{self.user.username} likes {self.content_object.title}"
        return self.user


class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return f"{self.user.username} dislikes {self.content_object.title}"
        return self.user


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    like = GenericRelation(Like)

    def __str__(self):
        return self.article.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at -= timedelta(days=365)
        super().save(*args, **kwargs)










