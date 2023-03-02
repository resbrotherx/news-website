from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'event'

urlpatterns = [
    path('', views.index, name="index"),
    path('event_detail/<id>/', views.event_detail, name='event_detail'),
]

