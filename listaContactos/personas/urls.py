from django.contrib import admin
from django.urls import path
from inicio.views import myHomeView, otraCosaVista

from personas.views import (personaTestView, 
personaCreateView, searchForHelp,personaAnotherCreateView, 
personaShowOBject, personaDeleteView, personaListView
)

app_name = 'personas'
urlpatterns = [
    path('agregar/', personaCreateView, name='createPersona'),
    path('search', searchForHelp, name='buscar'),
    path('anotherAdd',personaAnotherCreateView),
    path('<int:myID>/', personaShowOBject, name='browsing'),
    path('<int:myID>/delete',personaDeleteView,name='borrar'),
    path('',personaListView,name='lista'),
    
]

