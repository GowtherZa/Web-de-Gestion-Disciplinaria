from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User



cat_docentes = (
    ("-----","-----"),
    ("Titular","Titular"),
    ("Adiestrado","Adiestrado"),
    ("Instructor","Instructor"),
)

cargos = (
    ("-----","-----"),
    ("Instructor","Profesor"),
    ("J. Apto","J. Apto"),
    ("J. Asig","J. Asig"),
)

roles =(
 ("Usuario","Usuario"),
 ("Admin","Admin")
)

class perfil(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50) # Valorar cambiar a charfield
    cargo = models.CharField(max_length=15,choices=cargos,default=1)
    rol = models.CharField(max_length=15,choices=roles,default=1)
    cat_d = models.CharField(max_length=15,choices=cat_docentes,default=1)
    un_pass = models.CharField(max_length=30,default="") # Unencrypted pass

    class Meta:
        verbose_name_plural = 'perfiles'

    @property 
    def es_admin(self):
        return self.rol == "Admin"

    def __str__(self):
        return str(self.user)    

class denuncia(models.Model):
    texto = models.CharField(max_length=300)
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=50)
    fecha = models.DateField()  # Valorar cambiar a date
    hora = models.TimeField()
    area = models.CharField(max_length=50)
    usuario_d = models.CharField(max_length=10)
    estado = models.CharField(max_length=9,default="Pendiente")
    asignada = models.CharField(max_length=2,default="No")
    usuario = models.ForeignKey(User,on_delete=models.PROTECT,related_name='denuncias') 
    fecha_asignada = models.DateField(null="True")
    # comision 
    # expediente 

    @property
    def es_valida(self):
        return self.valida

    @property
    def es_asignada(self):
        # validar asignada = (len(comision))>0
        return self.asignada

    def __str__(self):
        return str(f'{self.usuario.username} -> {self.usuario_d}')   

class expediente(models.Model):

    texto = models.CharField(max_length=300)
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50) # Valorar cambiar a charfield
    anno_ac = models.CharField(max_length=9)
    fecha = models.DateField()  # Valorar cambiar a date
    grupo = models.CharField(max_length=4) 
    denuncia = models.OneToOneField(denuncia,on_delete=models.CASCADE,null=True)
    # usuario

class comision(models.Model):
    presidente = models.CharField(max_length=10)
    secretario = models.CharField(max_length=10)
    p_guia = models.CharField(max_length=10)
    v_feu = models.CharField(max_length=10)
    otros = models.CharField(max_length=300)
    # fecha_creacion = models.DateTimeField(default=timezone.now)
    dias_utiles = models.IntegerField(default=30)
    # denuncias

    class Meta:
        verbose_name_plural = 'comisiones'
