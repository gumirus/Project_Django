from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse('<h1>Моя первая страница</h1>')

def page2(request):
  return HttpResponse('<h1>Это вторая страница</h1>')
# Create your views here.
