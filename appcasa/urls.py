from django.urls import path
from appcasa.views import principio, gimnasio, listado_personas


urlpatterns = [
    path('', principio, name = 'principio'),
    path('gimnasio/', gimnasio, name = 'gimnasio'),
    path('listado/', listado_personas, name = 'listado_personas')
]

