from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(requests):
    return HttpResponse('welcome this is home page!!')

def kuchbhi_app_say_hello(request):
    return HttpResponse('hello this kuchbhi app main page !!')

def kuchbhi_app_hello_say_hello(request):
    return HttpResponse('hello buddy this is kuchbhi app hello page !!')

def hello_using_render(request):
    return render(request,'hello.html', {'name': 'Jeet'})