from django.contrib import admin
from .models import Genero, Artista, UsuarioCliente ,Productos
# Register your models here.
admin.site.register(Genero)
admin.site.register(Artista)
admin.site.register(UsuarioCliente)
admin.site.register(Productos)
