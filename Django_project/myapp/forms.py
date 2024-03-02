from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .choises import GENDER_CHOICES, ENGLISH_LEVEL_CHOICES


class CommentForm(forms.Form):
    comment = forms.CharField(label='parent_comment', required=True)

    def clean_comment(self):
        comment = self.cleaned_data.get('comment')
        return comment


class RecruiterForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name')
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label='Gender')
    age = forms.IntegerField(label='Возраст')
    english_level = forms.ChoiceField(choices=ENGLISH_LEVEL_CHOICES, label='English level')

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

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if user is None or not user.is_active:
                raise forms.ValidationError("Invalid username or password")

        return cleaned_data


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(label='Current password', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label='New password', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Confirmation of new password', widget=forms.PasswordInput)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        current_password = cleaned_data.get('current_password')
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')

        if new_password1 != new_password2:
            raise forms.ValidationError("new password and user do not match")

        user = authenticate(username=self.user.username, password=current_password)
        if user is None:
            raise forms.ValidationError('invalid current pass')

        self.user.set_password(new_password1)
        self.user.save()

        return cleaned_data
