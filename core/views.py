from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
# from django.contrib.auth.models import User
from .forms import *
from django.contrib import messages 
from .models import comision,denuncia,expediente, perfil
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required


@login_required
def denuncias(request):
    denuncias = denuncia.objects.all
    cant = denuncia.objects.count() == 0
    context = {'denuncias':denuncias,'hay_denuncias':cant}
    return render(request,'denuncias.html',context)

@login_required
def usuarios(request):
    perfiles = perfil.objects.all
    cant = perfil.objects.count() == 0
    context = {'perfiles':perfiles,'hay_perfiles':cant}
    return render(request,'usuarios.html',context)

@login_required
def comisiones(request):
    comisiones = comision.objects.all
    cant = comision.objects.count() == 0
    context = {'comisiones':comisiones,'hay_comisiones':cant}
    return render(request,'comisiones.html',context)

def index(request):
    return render(request,'index.html')

#  Formularios:
@login_required
def f_denuncia(request):

    if request.method == 'POST':
        print("________VALID_________")
        form = DenunciaForm(request.POST)
        
        if form.is_valid() :
            # Guardamos el usuario
            form.save() 

            messages.success(request, f'Denuncia creada')
            return redirect('denuncias')
    else:
        
        form = DenunciaForm()   
        
    context = {'form':form}

    return render(request,'crear_denuncia.html',context)

@login_required
def f_usuario(request):

    if request.method == 'POST':
        print("________VALID_________")
        user_form = UserRegisterForm(request.POST)
        profile_form = UserProfileRegisterForm(request.POST,initial=[])
        if user_form.is_valid() and profile_form.is_valid():
            # Guardamos el usuario
            user_form.save() 

            # Extraemos los datos del usuario y ciframos el pass
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
           
            usuario = User.objects.get(username=username)
            usuario.set_password(password)
            usuario.save()
            
            # Extraemos los datos del perfil y lo guardamos 

            nombre = profile_form.cleaned_data['nombre']
            apellidos = profile_form.cleaned_data['apellidos']
            correo = profile_form.cleaned_data['correo']
            cat_docente = profile_form.cleaned_data['cat_docente']
            rol = profile_form.cleaned_data['rol']
            cargo = profile_form.cleaned_data['cargo']

            profile = perfil.objects.create(nombre=nombre ,apellidos=apellidos ,correo=correo ,cargo=cargo ,rol=rol ,cat_d=cat_docente ,un_pass=password)
            perfil.objects.filter(user=usuario).update(user=usuario)
    
            profile.user = usuario
            profile.save()

            messages.success(request, f'Usuario {username} creado')
            return redirect('usuarios')
    else:
        
        user_form = UserRegisterForm()   
        profile_form = UserProfileRegisterForm()
        
    context = {'user_form':user_form,'profile_form':profile_form} 
    return render(request,'crear_usuario.html',context)

@login_required
def f_comision(request):
    return render(request,'modificar_comision.html')


#  Modificables: 
@login_required
def m_denuncia(request,id):

    denuncia_i = get_object_or_404(denuncia,id=id)
    
    form = DenunciaForm(instance=denuncia_i)

    context = {'id':id,'form':form}

    if request.method == 'POST':
    
        form = DenunciaForm(request.POST)

        if form.is_valid() :
            
            # Actualizamos la denuncia
            nombre = form.cleaned_data['nombre']
            apellidos = form.cleaned_data['apellidos']
            fecha = form.cleaned_data['fecha'] # Debe modificarse para que se retorne en el formato correcto
            hora = form.cleaned_data['hora'] # Debe modificarse para que se retorne en el formato correcto
            area = form.cleaned_data['area']
            usuario_d = form.cleaned_data['usuario_d']
            usuario = form.cleaned_data['usuario']
            texto = form.cleaned_data['texto']

            denuncia.objects.filter(id=id).update(nombre=nombre,apellidos=apellidos,fecha=fecha,hora=hora,area=area,usuario=usuario,usuario_d=usuario_d,texto=texto)

            messages.success(request, f'Denuncia modificada')

            return redirect('denuncias')

    return render(request,'modificar_denuncia.html',context)

@login_required
def m_usuario(request,id):

    usuario = get_object_or_404(User,id=id)
    
    user_data = {
        'username':usuario.username,
        'password' : usuario.perfil.un_pass
    }

    user_form = UserRegisterForm(instance=usuario,data=user_data)
    
    profile_data={
        'user':usuario,
        'nombre':usuario.perfil.nombre,
        'apellidos':usuario.perfil.apellidos,
        'correo':usuario.perfil.correo,
        'cat_docente':usuario.perfil.cat_d,
        'rol':usuario.perfil.rol,
        'cargo':usuario.perfil.cargo,
        'un_pass':usuario.password
    }

    profile_form = UserProfileRegisterForm(data=profile_data)

    context = {'id':id,'user_form':user_form,'profile_form':profile_form,'usuario':usuario}

    if request.method == 'POST':
        user_form = UserRegisterForm(data=request.POST,instance=usuario)
        profile_form = UserProfileRegisterForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            
            user_form.save()

            # Creamos el perfil y lo guardamos
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
           
            nombre = profile_form.cleaned_data['nombre']
            apellidos = profile_form.cleaned_data['apellidos']
            correo = profile_form.cleaned_data['correo']
            cat_docente = profile_form.cleaned_data['cat_docente']
            rol = profile_form.cleaned_data['rol']
            cargo = profile_form.cleaned_data['cargo']

            usuario = User.objects.get(username=username)
            usuario.set_password(password)
            usuario.save()
            perfil.objects.filter(user=usuario).update(nombre=nombre ,apellidos=apellidos ,correo=correo ,cargo=cargo ,rol=rol ,cat_d=cat_docente ,un_pass=password)
            
            messages.success(request, f'Usuario {username} modificado')

            return redirect('usuarios')
            
        context['user_form'] = user_form
        context['profile_form'] = profile_form

    return render(request,'modificar_usuario.html',context)

@login_required
def m_expediente(request):
    return render(request,'modificar_expediente.html')

@login_required
def m_comision(request):
    return render(request,'modificar_comision.html')

@login_required
def e_usuario(request,id):

    usuario = get_object_or_404(User,id=id)
    
    user_data = {
        'username':usuario.username,
        'password' : usuario.perfil.un_pass
    }

    user_form = UserRegisterForm(instance=usuario,data=user_data)
    
    profile_data={
        'user':usuario,
        'nombre':usuario.perfil.nombre,
        'apellidos':usuario.perfil.apellidos,
        'correo':usuario.perfil.correo,
        'cat_docente':usuario.perfil.cat_d,
        'rol':usuario.perfil.rol,
        'cargo':usuario.perfil.cargo,
        'un_pass':usuario.password
    }

    profile_form = UserProfileRegisterForm(data=profile_data)

    context = {'id':id,'user_form':user_form,'profile_form':profile_form,'usuario':usuario}

    if request.method == "POST":
        print("A POST")
        username = usuario.username
        usuario.delete()

        messages.success(request, f'Usuario {username} eliminado')

        return redirect('usuarios')

    print("NOT A POST")

    return render(request,'eliminar_usuario.html',context)

@login_required
def e_comision(request,id):

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