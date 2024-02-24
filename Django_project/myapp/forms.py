from django import forms
from django.core.exceptions import ValidationError


class CommentForm(forms.Form):
    comment = forms.CharField(label='parent_comment')

    def clean_comment(self):
        comment = self.cleaned_data.get('comment')
        if not comment:
            raise ValidationError('Age should be number')
        return comment


class RecruiterForm(forms.Form):
    name = forms.CharField(max_length=100)
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female')])
    age = forms.IntegerField()
    english_level = forms.ChoiceField(choices=[
        ('A1', 'A1'), ('A2', 'A2'), ('B1', 'B1'), ('B2', 'B2'), ('C1', 'C1'), ('C2', 'C2')
    ])

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



