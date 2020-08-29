from urllib import request
from django import forms
from crispy_forms.helper import FormHelper

from .models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'body')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['name'].label = "Username:"
        self.fields['name'].widget.attrs['readonly'] = True
        self.fields['body'].label = "Comment:"
