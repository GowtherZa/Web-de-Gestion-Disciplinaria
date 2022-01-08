from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime,date


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

class comision(models.Model):
    presidente = models.ForeignKey(User,on_delete=models.PROTECT,related_name='comision_presidente',null=True)
    secretario =  models.ForeignKey(User,on_delete=models.PROTECT,related_name='comision_secretario',null=True)
    p_guia =  models.ForeignKey(User,on_delete=models.PROTECT,related_name='comision_p_guia',null=True)
    v_feu = models.ForeignKey(User,on_delete=models.PROTECT,related_name='comision_v_feu',null=True)
    otros = models.CharField(max_length=300,null="True")
    dias_utiles = models.IntegerField(default=30)

    class Meta:
        verbose_name_plural = 'comisiones'

class expediente(models.Model):

    texto = models.CharField(max_length=300)
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50) # Valorar cambiar a charfield
    anno_ac = models.CharField(max_length=9)
    fecha = models.DateField()  # Valorar cambiar a date
    grupo = models.CharField(max_length=4) 
    # usuario

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

    # 1 denuncia solo pertenece a 1 comision, 1 comision tiene varias denuncias
    #comision_a = models.ForeignKey(comision, on_delete=models.PROTECT,null=True) 
    
    # 1 denuncia puede pertenecer a varias comisiones, 1 comision tiene varias denuncias
    comision_a = models.ManyToManyField(comision) 

    expediente = models.OneToOneField(expediente,on_delete=models.PROTECT,null=True)
    
    @property
    def es_valida(self):
        return self.valida

    @property
    def es_asignada(self):
        # validar asignada = (len(comision))>0
        return self.asignada
    
    @property
    def vida_util_de_asignada(self):
        f_asignada = self.fecha_asignada
        f_asignada = date(year=f_asignada.year,month=f_asignada.month,day=f_asignada.day)
        f_actual = date.today()
        dias = f_actual - f_asignada
        if dias == "0:00:00":
            dias = "Vencio hoy"
        else:
            dias = 30 - dias.days
            if int(dias) < 0 :
                dias = f"Vencida hace {dias*-1}"
        return dias

    def actualizar_creacion(self):
        self.fecha_asignada = datetime.today()

    def actualizar_asignada(self):
        if self.asignada == "No":
            self.asignada = "Si"
        else:
            self.asignada = "No"

    def __str__(self):
        return str(f'{self.usuario.username} -> {self.usuario_d}')   



