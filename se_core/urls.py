from django.urls import path, include
from django.contrib.auth import authenticate, login, logout

from se_core.vistas.navegacion.principal import index, acercaDe, contactanos, misionYVision, iniciarSesion, registrarme

urlpatterns = [
    # rutas de navegación inicial
    path('', index, name='index'),
    path('acerca_de/', acercaDe, name='acercade'),
    path('mision_y_vision/', misionYVision, name='misionyvision'),
    path('contactanos/', contactanos, name='contactanos'),
    path('login/', iniciarSesion, name='iniciar_sesion'),
    path('registro/', registrarme, name='registrarme'),
]