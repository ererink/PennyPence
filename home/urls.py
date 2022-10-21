from django.urls import path
from . import views

app_name='home'

urlpatterns = [
    path('',views.index,name='home'),
    path('wearepp/',views.wearepp,name='wearepp'),
]
