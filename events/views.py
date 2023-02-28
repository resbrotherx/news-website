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
    event = Event.objects.all().order_by('-date_updated')[0:1]
    events = Event.objects.all()
    popular = Event.objects.filter(popular=True).order_by('-date_updated')[0:3]
    if request.method == 'POST':
        email = request.POST.get('EMAIL')
        Email.objects.create(emais=email)
    constant = {
        'event':event,
        'events':events,
        'popular':popular
    }
    return render(request,"events.html",{'event':event})