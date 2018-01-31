
from django.shortcuts import render

def huy(request):
    return render(request, 'huy.html')

def govno(request):
    return render(request, 'govno.html')

def index(request):
    return render(request, 'index.html')