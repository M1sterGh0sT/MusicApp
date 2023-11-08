from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse



def index(request):
    return render(request, 'pages/index.html')



def index2(request):
    return render(request, 'pages/index2.html')





