"""GDU URL Configuration

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

from django.urls.conf import include
from . import views
from django.contrib import admin
from django.urls import path
import core.views 

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('',core.views.index, name='index'),
    path('',include('django.contrib.auth.urls')),
    # path('',Core.views.test),
    path('denuncias/',core.views.denuncias, name='denuncias'),
    path('usuarios/',core.views.usuarios, name='usuarios'),
    path('comisiones/',core.views.comisiones, name='comisiones'),
    path('f_denuncia/',core.views.f_denuncia, name='f_denuncia'),
    path('f_comision/',core.views.f_comision, name='f_comision'),
    path('f_usuario/',core.views.f_usuario, name='f_usuario'),
    path('m_denuncia/<id>/',core.views.m_denuncia, name='m_denuncia'),
    path('m_comision/<id>/',core.views.m_comision, name='m_comision'),
    path('m_usuario/<id>/',core.views.m_usuario, name='m_usuario'),
    path('m_comision/modificar_expediente.html/',core.views.m_expediente, name='m_expediente'),
    path('e_comision/<id>/',core.views.e_comision,name='e_comision'),
    path('e_usuario/<id>/',core.views.e_usuario,name='e_usuario'),
    path('i_denuncia/<id>/',core.views.i_denuncia,name='i_denuncia')
]
