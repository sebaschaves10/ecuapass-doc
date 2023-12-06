from django.shortcuts import render

# Create your views here.

from .models import Empresa, Conductor, Vehiculo, Cartaporte, Manifiesto

def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_empresas = Empresa.objects.all().count()
    num_conductors = Conductor.objects.all().count()
    num_vehiculos = Vehiculo.objects.all().count()
    num_cartaportes = Cartaporte.objects.all().count()
    num_manifestos = Manifiesto.objects.all().count()
    
    
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_empresas':num_empresas,'num_conductors':num_conductors,'num_vehiculos':num_vehiculos,'num_cartaportes':num_cartaportes, 'num_manifiestos':num_manifestos,'num_visits': num_visits},
    )

from django.views import generic

class CartaporteListView(generic.ListView):
    model = Cartaporte
class CartaporteDetailView(generic.DetailView):
    model = Cartaporte

class EmpresaListView(generic.ListView):
    model = Empresa
class EmpresaDetailView(generic.DetailView):
    model = Empresa
    
class ConductorListView(generic.ListView):
    model = Conductor
class ConductorDetailView(generic.DetailView):
    model = Conductor

class VehiculoListView(generic.ListView):
    model = Vehiculo
class VehiculoDetailView(generic.DetailView):
    model = Vehiculo

class ManifiestoListView(generic.ListView):
    model = Manifiesto
class ManifiestoDetailView(generic.DetailView):
    model = Manifiesto

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class EmpresaCreate(CreateView):
    model = Empresa
    fields = '__all__'
class EmpresaUpdate(UpdateView):
    model = Empresa
    fields = ['tipoId','nombre','direccion','ciudad', 'pais']
class EmpresaDelete(DeleteView):
    model = Empresa
    success_url = reverse_lazy('empresas')

class VehiculoCreate(CreateView):
    model = Vehiculo
    fields = '__all__'
class VehiculoUpdate(UpdateView):
    model = Vehiculo
    fields = ['pais','marca','chasis','fabricacion']
class VehiculoDelete(DeleteView):
    model = Vehiculo
    success_url = reverse_lazy('vehiculos')

class ConductorCreate(CreateView):
    model = Conductor
    fields = '__all__'
class ConductorUpdate(UpdateView):
    model = Conductor
    fields = ['nombre','nacionalidad','licencia','fecha_nacimiento']
class ConductorDelete(DeleteView):
    model = Conductor
    success_url = reverse_lazy('conductors')

class CartaporteCreate(CreateView):
    model = Cartaporte
    fields = '__all__'
class CartaporteUpdate(UpdateView):
    model = Cartaporte
    fields = ['tipo','remitente','destinatario','fecha_emision']
class CartaporteDelete(DeleteView):
    model = Cartaporte
    success_url = reverse_lazy('cartaportes')

class ManifiestoCreate(CreateView):
    model = Manifiesto
    fields = '__all__'
class ManifiestoUpdate(UpdateView):
    model = Manifiesto
    fields = ['tipo','conductor','vehiculo', 'cartaporte', 'fecha_emision']
class ManifiestoDelete(DeleteView):
    model = Manifiesto
    success_url = reverse_lazy('manifiestos')