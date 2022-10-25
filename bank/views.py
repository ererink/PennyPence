import imp
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BankForm, CommentForm
from .models import Bank, Comment

# Create your views here.
def index(request):
    return render(request, "bank/index.html")


def detail(request):
    return render(request, "bank/detail.html")


def search(request):
    return render(request, "bank/search.html")


def words(request):
    return render(request, "bank/words.html")
