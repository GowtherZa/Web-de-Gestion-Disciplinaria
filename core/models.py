from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User

# class usuario(User):
#     user = models.OneToOneField('settings.AUTH_USER_MODEL',on_delete=models.CASCADE)
#     telefono = models.CharField('Télefono', max_length=15)
#     avatar = models.ImageField('avatar para tu perfil', upload_to='avatars/', blank=True, null=True)
#     fondo = models.ImageField('Elige tu fondo de perfil', upload_to='fondos/', blank=True, null=True)

# class usuario(models.Model): # Debe ser extendido al usuario de django/admin
#     usuario = models.CharField(max_length=10)
#     nombre = models.CharField(max_length=20)
#     apellidos = models.CharField(max_length=50)
#     correo = models.EmailField(max_length=50) # Valorar cambiar a charfield
#     password = models.CharField(max_length=20)
#     cargo = models.CharField(max_length=20)
#     rol = models.CharField(max_length=20)
#     permisos = models.CharField(max_length=1)
#     # comisiones 
#     # denuncias

class denuncia(models.Model):
    texto = models.CharField(max_length=300)
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=50)
    fecha = models.CharField(max_length=8)  # Valorar cambiar a date
    hora = models.CharField(max_length=5)
    area = models.CharField(max_length=150)
    usuario_d = models.CharField(max_length=10)
    estado = models.CharField(max_length=9,default="Pendiente")
    asignada = models.CharField(max_length=2,default="No")
    # usuario 
    # comision 
    # expediente

    @property
    def es_valida(self):
        return self.valida

    @property
    def es_asignada(self):
        # validar asignada = (len(comision))>0
        return self.asignada

class expediente(models.Model):

    texto = models.CharField(max_length=300)
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50) # Valorar cambiar a charfield
    anno_ac = models.CharField(max_length=9)
    fecha = models.CharField(max_length=8)  # Valorar cambiar a date
    grupo = models.CharField(max_length=4) 
    # usuario
    # denuncia

class comision(models.Model):
    presidente = models.CharField(max_length=10)
    secretario = models.CharField(max_length=10)
    p_guia = models.CharField(max_length=10)
    v_feu = models.CharField(max_length=10)
    otros = models.CharField(max_length=300)
    # fecha_creacion = models.DateTimeField(default=timezone.now)
    dias_utiles = models.IntegerField(default=30)
    # denuncias
    
