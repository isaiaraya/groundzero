from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator

# Create your models here.
class Genero(models.Model):
    id_genero = models.AutoField(db_column='idGenero', primary_key=True)
    genero = models.CharField(max_length=20, blank=False, null=False)
    def __str__(self):
        return str(self.genero)
    

class Artista(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    id_genero = models.ForeignKey('Genero',on_delete=models.CASCADE, db_column='idGenero')
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    activo = models.IntegerField()
    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)
    
class UsuarioCliente(models.Model):
    nombre= models.CharField(max_length=40)
    correo= models.CharField(max_length=60)
    Contraseña= models.CharField(max_length=40)
    Numero_de_telefono= models.IntegerField(validators=[MaxValueValidator(999999999)])
    def __str__(self):
        return self.nombre
    

class Productos(models.Model):
    nombre= models.CharField(max_length=80)
    precio= models.IntegerField()
    tecnica= models.CharField(max_length=40)
    imagen= models.ImageField(upload_to="Productos", null=True)
    def __str__(self):
        return self.nombre

