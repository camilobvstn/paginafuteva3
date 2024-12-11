from django.shortcuts import render,redirect,get_object_or_404
from .models import Partido,Comentario
from .forms import PartidoForm,CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import response
from eva3.serializers import PartidoSerializer, ComentarioSerializer
from rest_framework.response import Response
from rest_framework import viewsets



def index(request):
    partidos=Partido.objects.all()
    data={'partidos':partidos}
    return render(request,'eva3/index.html',data)

@login_required
def registrarpartido(request):
    if request.method == 'POST':
        formulario = PartidoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/') 
        else:
            return render(request, 'eva3/registrarpartido.html', {'form': formulario}) 
    else:
        formulario = PartidoForm() 
    return render(request, 'eva3/registrarpartido.html', {'form': formulario})  

@login_required
def listapartidos(request):
    partidos=Partido.objects.all()
    data={'partidos':partidos}
    return render(request,'eva3/listapartidos.html',data)

@login_required
def modificarpartido(request,id):
    partido=get_object_or_404(Partido,id=id)
    data={'form':PartidoForm(instance=partido)}
    if request.method == 'POST':
        formulario = PartidoForm(data=request.POST,instance=partido , files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"El partido se modifico con exito")
            return redirect('/lista-partido') 
        else:
            return render(request, 'eva3/registrarpartido.html', {'form': formulario}) 
    else:
        formulario = PartidoForm() 

    return render(request,'eva3/modificarpartido.html',data)

@login_required
def eliminarpartido(request,id):
    partido=get_object_or_404(Partido, id=id)
    partido.delete()
    messages.success(request,"El partido se elimino correctamente")
    return redirect('/lista-partido') 

def registrousuario(request):
    data = {'form': CustomUserCreationForm()}

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            if user is not None:
                login(request, user) 
                return redirect(to='index') 
            data['form'] = formulario
        
    return render(request, 'registration/registro.html', data)

@login_required
def crear_comentario(request):
    if request.method == 'POST':
        partido_id = request.POST.get('partido')
        texto = request.POST.get('texto')
        comentario = Comentario(usuario=request.user, partido_id=partido_id, texto=texto)
        comentario.save()
        return redirect(to='index') 

    partidos = Partido.objects.all()
    return render(request, 'eva3/registrarcomentario.html', {'partidos': partidos})

@login_required
def ver_comentarios(request, partido_id):
    partido = get_object_or_404(Partido, id=partido_id)
    comentarios = Comentario.objects.filter(partido=partido)

    return render(request, 'eva3/ver_comentarios.html', {
        'partido': partido,
        'comentarios': comentarios,
    })

@login_required
def lista_comentarios(request):
    comentarios = Comentario.objects.all()
    data={'comentarios':comentarios}
    return render(request,'eva3/lista_comentarios.html',data)

@login_required
def actualizar_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)

    if request.method == 'POST':
        texto = request.POST.get('texto')
        comentario.texto = texto
        comentario.save()
        return redirect('ver-comentarios', partido_id=comentario.partido.id) 

    partidos = Partido.objects.all()
    return render(request, 'eva3/registrarcomentario.html', {
        'comentario': comentario,
        'partidos': partidos,
        'usuario': comentario.usuario,
    })

@login_required
def eliminar_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)
    comentario.delete()
    return redirect('lista-comentarios')


class PartidoViewSet(viewsets.ModelViewSet):
    queryset=Partido.objects.all()
    serializer_class= PartidoSerializer
