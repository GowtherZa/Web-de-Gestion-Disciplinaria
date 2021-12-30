from django.contrib import admin
from .models import comision,denuncia,expediente #,usuario

# Register your models here.
# admin.site.register(usuario)
admin.site.register(comision)
admin.site.register(denuncia)
admin.site.register(expediente)