from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'webify'

urlpatterns = [
    path('', views.index, name="index"),
    path('/news', views.news, name="news"),
    path('/about', views.about, name="about"),
    path('/contact', views.contact, name="contact"),
]

