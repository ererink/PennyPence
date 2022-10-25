from django.urls import path
from . import views

app_name = "stock"

urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("news/", views.news, name='news'),
    path("<int:pk>/", views.word, name="word"),
    path('create/', views.create, name='create'),
]
