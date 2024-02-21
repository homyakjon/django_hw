from django import forms
from django.core.exceptions import ValidationError


class CommentForm(forms.Form):
    comment = forms.CharField(label='parent_comment')

    def clean_comment(self):
        comment = self.cleaned_data.get('comment')
        if not comment:
            raise ValidationError('Age should be odd')
        return comment



