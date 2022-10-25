from django.urls import path
from . import views

app_name = "bank"

urlpatterns = [
    path("index/", views.index, name="index"),
    path("detail/", views.detail, name="detail"),
    path("search/", views.search, name="search"),
    path("words/", views.words, name="words"),
]
