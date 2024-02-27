from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .choises import GENDER_CHOICES, ENGLISH_LEVEL_CHOICES


class CommentForm(forms.Form):
    comment = forms.CharField(label='parent_comment', required=True)

    def clean_comment(self):
        comment = self.cleaned_data.get('comment')
        return comment


class RecruiterForm(forms.Form):
    name = forms.CharField(max_length=100, label='Имя')
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label='Пол')
    age = forms.IntegerField(label='Возраст')
    english_level = forms.ChoiceField(choices=ENGLISH_LEVEL_CHOICES, label='Уровень английского')

    def recruiter_validate(self):
        cleaned_data = super().clean()
        gender = cleaned_data.get('gender')
        age = cleaned_data.get('age')
        english_level = cleaned_data.get('english_level')

        if (gender == 'male' and age >= 20 and english_level in ['B2', 'C1', 'C2']) or \
           (gender == 'female' and age >= 22 and english_level in ['B1', 'B2', 'C1', 'C2']):
            return True
        else:
            return False


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

    def save(self):
        user = super().save()
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields.pop('username', None)
        self.fields.pop('password', None)


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(label='Текущий пароль', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label='Новый пароль', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Подтверждение нового пароля', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')

        if new_password1 != new_password2:
            raise forms.ValidationError('Новый пароль и его подтверждение не совпадают.')

        return cleaned_data
