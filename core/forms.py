from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    usuario = forms.CharField()
    password = forms.CharField()
    nombre = forms.CharField()
    apellidos = forms.CharField()
    correo = forms.EmailField()
    cat_docente = forms.ChoiceField()
    rol = forms.ChoiceField()
    cargo = forms.ChoiceField()
    # denuncias = array()
    # comisiones = array()
    # permisos = forms.ChoiceField()

    # cat_docente = forms.ChoiceField(choices=['Titular','Adiestrado','Instructor'])
    # rol = forms.ChoiceField(choices=['Usuario','Admin'])
    # cargo = forms.ChoiceField(choices=['Profesor','J. Apto','J. Asig'])

    class Meta:
        model = User
        fields = ['usuario','correo','nombre','apellidos','correo','cat_docente','rol','cargo']
        help_texts = {k:"" for k in fields}


