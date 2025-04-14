from django.shortcuts import render, redirect
from appcasa.forms import GimnasioForm
from appcasa.models import gimnasio

def principio (request):
    return render (request, 'appcasa/principio.html')

def gimnasio (request):
    print('ESTOS SON LOS DATOS DEL GET', request.GET)
    print('ESTOS SON LOS DATOS DEL POST', request.POST)
    if request.method == 'POST':
        formulario = GimnasioForm(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            gym = gimnasio(nombre = info.get ('nombre'), apellido = info.get('apellido'))
            gym.save()
            return redirect ('listado_personas')
    else:
        formulario = GimnasioForm()
        
    return render (request, 'appcasa/gimnasio.html', {'formulario': formulario})
    
def listado_personas(request):
    personas = gimnasio.objects.all()
    return render(request, 'appcasa/listado.html', {'personas': personas})    

def listado_personas(request):
    gimnasio = gimnasio.objects.all()
    return render(request, 'Hpp/listado_personas.html', {'gimnasio':gimnasio})
