from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import denuncia, perfil

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

class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'input'}))
    password = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'input','type':'password'}))
    
    class Meta:
        model = User
        fields = ['username','password']
        help_texts = {k:"" for k in fields}
     
    def __init__(self,*args,**kwargs):
        super(forms.ModelForm,self).__init__(*args,**kwargs)

        self.fields['username'].widget.attrs['class'] = 'input'
        self.fields['password'].widget.attrs['class'] = 'input' 

        self.fields['username'].label= 'Usuario'
        self.fields['password'].label = 'Contraseña'
       
class UserProfileRegisterForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    apellidos = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    correo = forms.EmailField(widget=forms.EmailInput(attrs={'class':'input'}))
    cat_docente = forms.ChoiceField(choices=cat_docentes,widget=forms.Select(attrs={'class':' '}))
    rol = forms.ChoiceField(choices=roles,widget=forms.Select(attrs={'class':''}))
    cargo = forms.ChoiceField(choices=cargos,widget=forms.Select(attrs={'class':''}))
    
    class Meta:
        model = perfil
        fields = ['nombre','apellidos','correo','cat_docente','rol','cargo']
        help_texts = {k:"" for k in fields}

class DenunciaForm(forms.ModelForm):
    texto = forms.CharField(label="Descripción de la denuncia",widget=forms.Textarea(attrs={'class':'textarea','rows':2}))
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    apellidos = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    fecha = forms.DateField(input_formats=['%d/%m/%y','%y-%m-%d'],widget=forms.DateInput(attrs={'class':'input'}))
    hora = forms.TimeField(input_formats=['%H:%M','%H:%M:%S'],widget=forms.TimeInput(attrs={'class':'input'}))
    area = forms.CharField(label="Área",widget=forms.TextInput(attrs={'class':'input'}))
    usuario_d = forms.CharField(label="Usuario denunciado",widget=forms.TextInput(attrs={'class':'input'}))
    usuario = forms.ModelChoiceField(label="Usuario del denunciante",queryset=User.objects.all())

    class Meta:
        model = denuncia
        fields = ['nombre','apellidos','fecha','hora','area','usuario_d','usuario','texto']
        help_texts = {k:"" for k in fields}