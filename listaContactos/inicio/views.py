from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myHomeView(request,*args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request,'home.html')

def otraCosaVista(request):
    return HttpResponse('<h1>Otra cosa de contenido<h/1>')