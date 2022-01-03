from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User


cat_docentes = (
    ("1","-----"),
    ("2","Titular"),
    ("3","Adiestrado"),
    ("4","Instructor"),
)

cargos = (
    ("1","-----"),
    ("2","Profesor"),
    ("3","J. Apto"),
    ("4","J. Asig"),
)

roles =(
 ("1","Usuario"),
 ("2","Admin")
)
class perfil(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50) # Valorar cambiar a charfield
    cargo = models.CharField(max_length=8,choices=cargos,default="1")
    rol = models.CharField(max_length=7,choices=roles,default="1")
    cat_d = models.CharField(max_length=10,choices=cat_docentes,default="1")
    # comisiones 
    # denuncias

    @property 
    def es_admin(self):
        return self.rol == "Admin"

    def __str__(self):
        return str(self.user)    

class denuncia(models.Model):
    texto = models.CharField(max_length=300)
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=50)
    fecha = models.CharField(max_length=8)  # Valorar cambiar a date
    hora = models.CharField(max_length=5)
    area = models.CharField(max_length=150)
    usuario_d = models.CharField(max_length=10)
    estado = models.BooleanField(max_length=9,default="Pendiente")
    asignada = models.CharField(max_length=2,default="No")
    usuario = models.ForeignKey(User,on_delete=models.PROTECT,related_name='denuncias') 
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
    
