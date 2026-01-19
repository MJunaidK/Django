from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('create', views.create_post, name='create'),
    path('feed', views.feed, name='feed'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
   ]


