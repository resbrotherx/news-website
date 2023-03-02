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
    gallery = Gallery.objects.all().order_by('-date_updated')
    return render(request,"gallery.html",{'gallery':gallery})


