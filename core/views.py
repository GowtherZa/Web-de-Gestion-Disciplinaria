from django.shortcuts import render
# from django.contrib.auth.models import User
from .forms import UserRegisterForm
from django.contrib import messages 
from .models import comision,denuncia,expediente

def autorizacion(request): 
    return render(request,'autorizacion.html')

def denuncias(request):
    denuncias = denuncia.objects.all
    cant = denuncia.objects.count() == 0
    context = {'denuncias':denuncias,'hay_denuncias':cant}
    return render(request,'denuncias.html',context)

def usuarios(request):
    return render(request,'usuarios.html')

def comisiones(request):
    comisiones = comision.objects.all
    cant = comision.objects.count() == 0
    context = {'comisiones':comisiones,'hay_comisiones':cant}
    return render(request,'comisiones.html',context)

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


# Testeo
def test(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request,f'Usuario {username} creado')
    else:
        form = UserRegisterForm()
    
    context = {'form':form}
    return render(request,'modificar_comision.html',context)

    # usuario = User.objects.filter(username="Boza").exists()
    # if not usuario:
    #     usuario = User.objects.create(username="Boza",password="123")
    # else:
    #     usuario = User.objects.get(username="Boza")
    # return render(request,'test.html',{'usuario':usuario.perfil})
# 