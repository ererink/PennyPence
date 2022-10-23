from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Stock
from .forms import ArticleForm

# Create your views here.

def index(request):
    return render(request, 'stock/index.html')

def search(request):
    return render(request, 'stock/search.html')

def news(request):
    return render(request, 'stock/news.html')

def word(request):
    return render(request, 'stock/word.html')