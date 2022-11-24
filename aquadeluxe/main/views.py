from django.shortcuts import render
from main.models import *

# Create your views here.


def indexHandler(request):

    return render(request, 'index.html', {})


def thanksHandler(request):

    return render(request, 'thank-you.html', {})
