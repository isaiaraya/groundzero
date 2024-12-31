from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from .models import Artista,Genero
from django.contrib.auth.models import User
from .models import Productos
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate,login

def index(request):
    context={}
    return render(request, 'groundzero/index.html', context)

def Artistas(request):
    context={}
    return render (request,'groundzero/Artistas.html',context)

def catalogo(request):
    productos= Productos.objects.all()
    data= {
        'productos': productos
    }
    return render (request,'groundzero/catalogo.html',data)


def registro(request):
    data={
        'form': CustomUserCreationForm
    }

    if request.method  =='POST':
        formulario =CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user= authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password"])
            login(request,user)
            return redirect(to='home')
        data["form"]=formulario

    return render(request,'registration/registro.html',data)

def contacto(request):
    context={}
    return render (request,'groundzero/contacto.html',context)

def login(request):
    context={}
    return render (request,'groundzero/login.html',context)

def formulario(request):
    artistas=Artista.objects.all()
    context={"artistas":artistas}
    return render (request,'groundzero/formulario.html',context)


def crud(request):
    artistas = Artista.objects.all()
    context = {'artistas':artistas}
    return render(request, 'groundzero/artistas_list.html',context)

def artistasAdd(request):
    if request.method != "POST":
        generos=Genero.objects.all()
        context={'generos':generos}
        return render(request, 'groundzero/artistas_add.html',context)
    else:
        id=request.POST["id"]
        nombre=request.POST["nombre"]
        aPaterno=request.POST["paterno"]
        aMaterno=request.POST["materno"]
        fechaNac=request.POST["fechaNac"]
        genero=request.POST["genero"]
        email=request.POST["email"]
        activo="1"

        objGenero=Genero.objects.get(id_genero=genero)
        obj=Artista.objects.create( id=id,
                                    nombre=nombre,
                                    apellido_paterno=aPaterno,
                                    apellido_materno=aMaterno,
                                    fecha_nacimiento=fechaNac,
                                    id_genero=objGenero,
                                    
                                    email=email,
                                    activo=1)
        obj.save()
        context={'mensaje':"Ok, datos grabados!!."}
        return render(request,'groundzero/artistas_add.html', context) 
    



def artistas_del(request,pk):
    context={}
    try:
        artista=Artista.objects.get(id=pk)

        artista.delete()
        mensaje="Datos eliminados"
        artistas = Artista.objects.all()
        context = {'artistas': artistas, 'mensaje':mensaje}
        return render(request, 'groundzero/artistas_list.html',context)
    except:
        mensaje="Error, ID no existe"
        artistas = Artista.objects.all()
        context = {'artistas': artistas, 'mensaje':mensaje}
        return render(request, 'groundzero/artistas_list.html',context)
    


def artistas_findEdit(request,pk):
    if pk !="":
        artista=Artista.objects.get(id=pk)
        generos=Genero.objects.all()

        print(type(artista.id_genero.genero))

        context={'artista':artista,'generos':generos}
        if artista:
            return render(request,'groundzero/artistas_edit.html',context)
        else:
            context={'mensaje':"Error, ID no existe"}
            return render(request, 'groundzero/artistas_list.html',context)
        





def artistasUpdate(request):
    if request.method == "POST":
        id=request.POST["id"]
        nombre=request.POST["nombre"]
        aPaterno=request.POST["paterno"]
        aMaterno=request.POST["materno"]
        fechaNac=request.POST["fechaNac"]
        genero=request.POST["genero"]
        email=request.POST["email"]
        activo="1"

        objGenero=Genero.objects.get(id_genero=genero)
        
        artista = Artista()
        artista.id=id
        artista.nombre=nombre
        artista.apellido_paterno=aPaterno
        artista.apellido_materno=aMaterno
        artista.fecha_nacimiento=fechaNac
        artista.id_genero=objGenero
        artista.email=email
        artista.activo=1
        artista.save()
        generos=Genero.objects.all()
        context={'mensaje':"Ok, datos actualizados --.",'generos':generos,'artista':artista}
        return render(request,'groundzero/artistas_edit.html', context)
    else:
        artistas = Artista.objects.all()
        context={'artistas':artistas}
        return render(request,'groundzero/artistas_list.html', context)


def CrearUsuario(request):

    user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')
    user.first_name = 'John'
    user.last_name = 'Citizen'
    user.save()

    


