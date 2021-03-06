"""listaContactos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from inicio.views import myHomeView, otraCosaVista
from personas.views import (
    personaTestView, personaCreateView, 
    searchForHelp, personaCreateView2,personaAnotherCreateView,
    personaShowOBject, personaDeleteView, personaListView
)

urlpatterns = [
    path('persona/',include('personas.urls')),
    path('admin/', admin.site.urls),
    path('',myHomeView, name='Pagina de inicio'),
    path('otrapagina',otraCosaVista, name='otracosa'),
    #path('persona/', personaTestView, name='Otro'),
    #path('agregar/', personaCreateView, name='createPersona'),
    path('search', searchForHelp, name='buscar'),
    path('add', personaCreateView2, name='createPersona'),
    path('anotherAdd',personaAnotherCreateView,name='OtroAgregarPersonas'),
    #path('persona/<int:myID>/', personaShowOBject, name='browsing'),
    #path('persona/<int:myID>/delete',personaDeleteView,name='borrar'),
    #path('persona/',personaListView,name='lista')
]
