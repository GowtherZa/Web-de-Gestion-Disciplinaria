from django.contrib import admin
from .models import comision,denuncia,expediente,perfil

# Register your models here.
admin.site.register(perfil)
admin.site.register(comision)
admin.site.register(denuncia)
admin.site.register(expediente)