from django.urls import path
from .views import Inicio, Listado_telefonos, Detalle_telefono, Crear_telefono, Borrar_telefono,Modificar_telefono
urlpatterns = [
    path('',Inicio.as_view(),name='inicio'),
    path('listadoTelefonos/',Listado_telefonos.as_view(), name='listadoTelefonos'), #ruta para sacar el listado de
    path('detalleTelefono/<int:pk>/',Detalle_telefono.as_view(), name='detalleTelefono'),
    path('crearTelefono',Crear_telefono.as_view(),name='crearTelefono'),
    path('borrarTelefono/<int:pk>/',Borrar_telefono.as_view(), name='borrarTelefono'),
    path('modificarTelefono/<int:pk>/',Modificar_telefono.as_view(), name='modificarTelefono'),
]