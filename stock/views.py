from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm

# Create your views here.

def index(request):
    return render(request, 'stock/index.html')

def search(request):
    articles = Article.objects.order_by('-pk')

    context = {
        'articles': articles
    }
    return render(request, 'stock/search.html', context)

def news(request):
    return render(request, 'stock/news.html')

# detail
def word(request, pk):
    article = Article.objects.get(pk=pk)

    context = {
        'article': article,
    }
    return render(request, 'stock/word.html', context)

def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.user = request.user 
            article.save()
            messages.success(request, '게시물 작성 완료!')
            return redirect('stock:search')
    
    else: 
        article_form = ArticleForm()

    context = {
        'article_form': article_form
    }
    return render(request, 'stock/create.html', context=context)