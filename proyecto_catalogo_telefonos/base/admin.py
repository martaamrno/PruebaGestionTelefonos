from django.contrib import admin
from .models import Telefonos
# Register your models here.
@admin.register(Telefonos)
class TelefonoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fabricante','fecha_lanzamiento','precio','sistemaOperativo','disponibilidad','created_at', 'update_at',)
    search_fields= ('nombre',)
    readonly_fields = ('created_at', 'update_at')