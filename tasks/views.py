from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def helloworld(requests):
    return HttpResponse('Hello World')

def taskList(requests):
    return render(requests, 'task/list.html')

def yourname(requests, name):
    return render(requests, 'task/yourname.html', {'name': name})