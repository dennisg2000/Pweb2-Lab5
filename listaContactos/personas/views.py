from django.shortcuts import render

from .models import Persona
from .forms import PersonaForm, RawPersonaForm

# Create your views here.
def personaTestView(request):
    obj = Persona.objects.get(id=1)
    context = {
    'objeto' : obj,
    
    }
    return render(request, 'personas/descripcion.html', context) 

def personaCreateView(request):
    form = PersonaForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PersonaForm()
    context = {
        'form' : form
        }
    return render(request, 'personas/personasCreate.html', context)

def searchForHelp(request):
    return render(request, 'personas/search.html', {})

def personaCreateView2(request):
    #print('GET: ', request.GET)
    #print('POST: ', request.POST)
    print('hola')
    print(request)
    if request.method == 'POST':
        nombre= request.POST.get('q')
        print(nombre)
    context = {}
    return render(request, 'personas/personasCreate2.html', context)

def personaAnotherCreateView(request):
    form = RawPersonaForm()
    if request.method=="POST":
        form = RawPersonaForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Persona.objects.create(**form.cleaned_data)
        else:
            print (form.errors)
    context = {
        'form' : form,
    }
    return render(request,'personas/personasCreate.html',context)