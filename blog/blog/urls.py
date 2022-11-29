"""blog URL Configuration

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
from . import views

urlpatterns = [

    path('admin/', admin.site.urls),
    # 1 PARAMETROS ES EL TEXTO DE LA URL
    # 2 LA VISTA QUE VA EJECUTAR
    # 3 ES EL NOMBRE LA URL (aun no lo usamos)
    path('', views.Home, name = 'home'),

    #No necesariamente estos 3 valores (parametors) se deben llamar igual
    path('Nosotros/', views.Nosotros, name = 'nosotros'),


    # URL DE APLICACION
    path('Noticias/', include('apps.noticias.urls')),

]
