from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
import json
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import *
# from users.models import *
from django.db.models import Sum



def index(request):
    if request.method == 'POST':
        email = request.POST.get('EMAIL')
        print("this the email",email)
        Email.objects.create(emais=email)
    banners = New.objects.filter(futured=True).order_by('-date_updated')[0:2]
    lates = New.objects.filter(approved=True).order_by('-date_updated')[0:1]
    lates2 = New.objects.filter(approved=True).order_by('-date_updated')[1:2]
    news = New.objects.filter(approved=True)[0:1]
    news2 = New.objects.filter(approved=True)[2:3]
    banner = New.objects.filter(one=True).order_by('-date_updated')[0:1]
    # news = New.objects.all().order_by('-date_updated')[0:8]
    constant = {
        'lates':lates,
        'lates2':lates2,
        'banners':banners,
        'banner':banner,
        'news':news,
        'news2':news2
    }
    return render(request,"index.html",constant)


def about(request):
    if request.method == 'POST':
        email = request.POST.get('EMAIL')
        print("this the email",email)
        Email.objects.create(emais=email)
    pass
    return render(request,"kwabify/UserDashboard/finance-banks.html")


def contact(request):
    if request.method == 'POST':
        email = request.POST.get('EMAIL')
        print("this the email",email)
        Email.objects.create(emais=email)
    pass
    return render(request,"kwabify/UserDashboard/finance-banks.html")


def news(request):
    news = New.objects.all().order_by('-date_updated')
    popular = New.objects.filter(popular=True).order_by('-date_updated')[0:3]
    if request.method == 'POST':
        email = request.POST.get('EMAIL')
        print("this the email",email)
        Email.objects.create(emais=email)
    constant = {
        'news':news,
        'popular':popular
    }
    return render(request,"news.html",constant)