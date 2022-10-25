from django import forms
from .models import Bank, Comment


class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = [
            "title",
            "content",
            "image",
            "thumbnail",
        ]
        labels = {
            "title": "제목",
            "content": "내용",
            "image": "이미지",
            "thumbnail": "썸네일",
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "content",
        ]
        labels = {
            "content": "댓글",
        }
