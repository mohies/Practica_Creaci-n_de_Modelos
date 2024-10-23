from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.db.models import Avg,Max,Min
# Create your views here.
def index(request):
    return render(request, 'index.html')
