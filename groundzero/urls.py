from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('Artistas/', views.Artistas, name='Artistas'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('contacto/', views.contacto, name='contacto'),
    path('formulario/', views.formulario, name='formulario'),
    path('crud', views.crud, name='crud'),
    path('artistasAdd', views.artistasAdd, name='artistasAdd'),
    path('artistas_del/<str:pk>', views.artistas_del, name='artistas_del'),
    path('artistas_findEdit/<str:pk>', views.artistas_findEdit, name='artistas_findEdit'),
    path('artistasUpdate', views.artistasUpdate, name='artistasUpdate'),
    path('registro/', views.registro, name='registro'),

]
