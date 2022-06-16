from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myHomeView(request,*args, **kwargs):
    print(args, kwargs)
    print(request.user)
    myContext = {
        'myText' : "esto es sobre nosotros",
        'myNumber' : 123,
        'myList' :[33,44,55,66,77,88,44]
    }
    return render(request,'home.html',myContext)

def otraCosaVista(request):
    return HttpResponse('<h1>Otra cosa de contenido<h/1>')