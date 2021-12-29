from django.shortcuts import render
from django.contrib.auth.models import User

def autorizacion(request): 
    return render(request,'autorizacion.html')

def denuncias(request):
    return render(request,'denuncias.html')

def usuarios(request):
    return render(request,'usuarios.html')

def comisiones(request):
    return render(request,'comisiones.html')

def index(request):
    return render(request,'index.html')


#  Formularios:

def f_denuncia(request):
    return render(request,'modificar_denuncia.html')

def f_usuario(request):
    return render(request,'modificar_usuario.html')

def f_comision(request):
    return render(request,'modificar_comision.html')

# 

#  Modificables: 

def m_denuncia(request):
    return render(request,'modificar_denuncia.html')

def m_usuario(request):
    return render(request,'modificar_usuario.html')

def m_expediente(request):
    return render(request,'modificar_expediente.html')

def m_comision(request):
    return render(request,'modificar_comision.html')

def e_usuario(request):
    return render(request,'eliminar_usuario.html')

def e_comision(request):
    return render(request,'eliminar_comision.html')

# 
