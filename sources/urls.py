from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('news-sources', views.newsList, name = "news-sources"),
    
]