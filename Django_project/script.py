from django.contrib.auth.models import User
from myapp.models import Article, Comment


user = User.objects.create(
    username='Oliver',
    email='ol@gmail.com',
)
user.set_password('oliv555')
user.save()
print(user)

user1 = User.objects.create(
    username='Jake',
    email='j@gmail.com',
)
user1.set_password('j007')
user1.save()
print(user1)

user2 = User.objects.create(
    username='Connor',
    email='con@gmail.com',
)
user2.set_password('con777')
user2.save()
print(user2)

user3 = User.objects.create(
    username='Liam',
    email='liam@gmail.com',
)
user3.set_password('liam12')
user3.save()
print(user3)

user4 = User.objects.create(
    username='Harry',
    email='h@gmail.com',
)
user4.set_password('harry001')
user4.save()
print(user4)

user5 = User.objects.create(
    username='Mason',
    email='mas@gmail.com',
)
user5.set_password('mason88')
user5.save()
print(user5)

article = Article.objects.create(title='Hello Rock n roll', content='Article about rock n roll', author=user)
print(f'Created article {article}')

article1 = Article.objects.create(title='Animal jazz', content='Article about jazz', author=user1)
print(f'Created article {article1}')

article2 = Article.objects.create(title='Rammstein', content='Article about underground', author=user2)
print(f'Created article {article2}')

article3 = Article.objects.create(title='Manowar', content='Article about metal', author=user3)
print(f'Created article {article3}')

article4 = Article.objects.create(title='Scorpions', content='Article about heavy metal', author=user4)
print(f'Created article {article4}')

article5 = Article.objects.create(title='WigWam', content='Article about glam rock', author=user5)
print(f'Created article {article5}')

c = Comment.objects.create(content='Start music its now', author=user, article=article)

print(f'comment one: {c}')

c1 = Comment.objects.create(content='I am a Middle and you Junior', author=user, article=article1)
print(f'comment two: {c1}')

c2 = Comment.objects.create(content='You already on the Finish', author=user, article=article2)
print(f'comment three: {c2}')

c3 = Comment.objects.create(content='Hello everybody', author=user, article=article3)
print(f'comment four: {c3}')

c4 = Comment.objects.create(content='I know Elvis', author=user, article=article4)
print(f'comment five: {c4}')

c5 = Comment.objects.create(content='We are drawing a picture', author=user, article=article5)
print(f'comment six: {c5}')

last_five_comments_objects = Comment.objects.order_by('-created_at')[:5]
print(last_five_comments_objects)

last_five_comments_text = [comment.content for comment in last_five_comments_objects]
print(last_five_comments_text)

comments_to_change = Comment.objects.filter(
    content__icontains='Start'
) | Comment.objects.filter(
    content__icontains='Middle'
) | Comment.objects.filter(
    content__icontains='Finish'
)

for comment in comments_to_change:
    comment.content = (
        comment.content.replace('Start', 'Time')
                       .replace('Middle', 'Senior')
                       .replace('Finish', 'Home')
    )
    comment.save()

comments_to_delete = Comment.objects.filter(content__icontains='k').exclude(content__icontains='c')
comments_to_delete.delete()
print(f'deleted comments: {comments_to_delete}')

latest_author = Article.objects.latest('author__username')
print(latest_author)
comments_before_date = Comment.objects.filter(created_at__lt=latest_author.created_at)[:2]
print(comments_before_date)


# python manage.py shell < script.py > git_log.txt



