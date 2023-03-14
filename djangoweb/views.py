from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def say_hello(request):
    # return HttpResponse('Hello World')
    return render(request, 'index.html', {'name': simpson[0], 'dates':'1/1/2023'})

simpson = ['Lisa', 'Bart']

def say_hi(request):
    return render(request, 'about.html', {'name': simpson[1]})
