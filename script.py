from django.contrib.auth.models import User
from myapp.models import Article, Comment


user, created = User.objects.get_or_create(username='Philip', email='p@example.com', defaults={'password': 'pl111'})
print(user)

user1, created = User.objects.get_or_create(username='Bob', email='bob@example.com', defaults={'password': 'bob11'})
print(user1)

user2, created = User.objects.get_or_create(username='Lina', email='lin@example.com', defaults={'password': 'lin55'})
print(user2)

user3, created = User.objects.get_or_create(username='Anna', email='anna@example.com', defaults={'password': 'anna66'})
print(user3)

user4, created = User.objects.get_or_create(username='Will', email='will@example.com', defaults={'password': 'will20'})
print(user4)

user5, created = User.objects.get_or_create(username='Jim', email='jim@example.com', defaults={'password': 'jim000'})
print(user5)

article, created = Article.objects.get_or_create(title='Hello Rock n roll', content='Article about rock n roll', author=user)
print(f'Created article {article}')

article1, created = Article.objects.get_or_create(title='Animal jazz', content='Article about jazz', author=user1)
print(f'Created article {article1}')

article2, created = Article.objects.get_or_create(title='Rammstein', content='Article about underground', author=user2)
print(f'Created article {article2}')

article3, created = Article.objects.get_or_create(title='Manowar', content='Article about metal', author=user3)
print(f'Created article {article3}')

article4, created = Article.objects.get_or_create(title='Scorpions', content='Article about heavy metal', author=user4)
print(f'Created article {article4}')

article5, created = Article.objects.get_or_create(title='WigWam', content='Article about glam rock', author=user5)
print(f'Created article {article5}')

c, created = Comment.objects.get_or_create(content='Start music its now', author=user, article=article)
print(f'comment one: {c}')

c1, created = Comment.objects.get_or_create(content='I am a Middle and you Junior', author=user, article=article1)
print(f'comment two: {c1}')

c2, created = Comment.objects.get_or_create(content='You already on the Finish', author=user, article=article2)
print(f'comment three: {c2}')

c3, created = Comment.objects.get_or_create(content='Hello everybody', author=user, article=article3)
print(f'comment four: {c3}')

c4, created = Comment.objects.get_or_create(content='I know Elvis', author=user, article=article4)
print(f'comment five: {c4}')

c5, created = Comment.objects.get_or_create(content='We are drawing a picture', author=user, article=article5)
print(f'comment six: {c5}')


last_five_comments_objects = Comment.objects.order_by('-created_at')[:5]
print(last_five_comments_objects)

last_five_comments_text = [comment.content for comment in last_five_comments_objects]
print(last_five_comments_text)

comments_to_change = Comment.objects.filter(
    content__icontains='Start') | \
    Comment.objects.filter(content__icontains='Middle') | \
    Comment.objects.filter(content__icontains='Finish')

for comment in comments_to_change:
    comment.content = comment.content.replace('Start', 'Time') \
                                      .replace('Middle', 'Senior') \
                                      .replace('Finish', 'Home')
    comment.save()
    print(comments_to_change)

comments_to_delete = Comment.objects.filter(content__icontains='k').exclude(content__icontains='c')
comments_to_delete.delete()
print(f'deleted comments: {comments_to_delete}')

latest_author = Article.objects.latest('author__username')
print(latest_author)
comments_before_date = Comment.objects.filter(created_at__lt=latest_author.created_at)[:2]
print(comments_before_date)


# exec(open('script.py').read())
