from django.shortcuts import render
from django.http import HttpResponse

def helloWorld(request):
    return HttpResponse('hello world!')

def taskList(request):
    return render(request, 'tasks/list.html')

def yourName(request, name):
    return render(request, 'tasks/yourname.html',{'name':name})