from django import forms
from .models import article


class CreateArticle(forms.ModelForm):

    class Meta:
        model = article
        fields = ['title', 'slug', 'body', 'thumb']