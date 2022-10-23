from django import forms
from .models import Stock

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Stock
        fields = ['title', 'content', 'image', 'thumbnail']