"""paginafut URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from eva3.views import index,registrarpartido,listapartidos,modificarpartido,eliminarpartido,registrousuario,crear_comentario,ver_comentarios, actualizar_comentario,eliminar_comentario,lista_comentarios,PartidoViewSet
from django.conf import settings
from django.conf.urls.static import static 
from rest_framework import routers #esto

routers=routers.DefaultRouter() #esto
routers.register('partidoapi',PartidoViewSet)

#http://127.0.0.1:8000/api/partidoapi
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', index, name='index'),
    path('registrar-partido', registrarpartido, name='registrar-partido'),
    path('lista-partido', listapartidos, name='lista-partido'),
    path('modificar-partido/<id>/', modificarpartido, name='modificar-partido'),
    path('eliminar-partido/<id>/', eliminarpartido, name='eliminar-partido'),
    path('registrar-usuario', registrousuario, name='registrar-usuario'),
    path('registrar-comentario', crear_comentario, name='registrar-comentario'),
    path('partido/<int:partido_id>/comentarios/', ver_comentarios, name='ver-comentarios'),
    path('comentarios/', lista_comentarios, name='lista-comentarios'), 
    path('comentario/<int:comentario_id>/actualizar/', actualizar_comentario, name='actualizar-comentario'),
    path('comentario/<int:comentario_id>/eliminar/', eliminar_comentario, name='eliminar-comentario'),
    path('api/',include(routers.urls)), #esto
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
