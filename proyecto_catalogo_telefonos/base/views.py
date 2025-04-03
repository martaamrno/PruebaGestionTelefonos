from .models import Telefonos
from django.views.generic import TemplateView, ListView,DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
# Create your views here.
class Inicio(TemplateView):
    template_name = "base/inicio.html"

class Listado_telefonos(ListView):
    model = Telefonos
    template_name= "base/listadoTelefonos.html"
    context_object_name = "telefonos"

class Detalle_telefono(DetailView):
    model= Telefonos
    template_name= "base/detalleTelefono.html"
    context_object_name = "telefonos"

class Crear_telefono(CreateView):
    model=Telefonos
    fields="__all__"
    success_url = reverse_lazy('listadoTelefonos')

class Borrar_telefono(DeleteView):
    model= Telefonos
    success_url = reverse_lazy('listadoTelefonos')

class Modificar_telefono(UpdateView):
    model=Telefonos
    fields = '__all__'
    success_url = reverse_lazy('listadoTelefonos')