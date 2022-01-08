from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import comision, denuncia, perfil

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
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'input','placeholder':'Nombre de usuario'}))
    password = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'input','type':'password','placeholder':'Contraseña del usuario'}))
    
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
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'input', 'placeholder':'Nombre del usuario'}))
    apellidos = forms.CharField(widget=forms.TextInput(attrs={'class':'input','placeholder':'Apellidos del usuario'}))
    correo = forms.EmailField(widget=forms.EmailInput(attrs={'class':'input','placeholder':'Correo del usuario'}))
    cat_docente = forms.ChoiceField(choices=cat_docentes,widget=forms.Select(attrs={'class':'','placeholder':'Categoría docente del usuario'}))
    rol = forms.ChoiceField(choices=roles,widget=forms.Select(attrs={'class':'','placeholder':'Rol del usuario'}))
    cargo = forms.ChoiceField(choices=cargos,widget=forms.Select(attrs={'class':'','placeholder':'Cargo del usuario'}))
    
    class Meta:
        model = perfil
        fields = ['nombre','apellidos','correo','cat_docente','rol','cargo']
        help_texts = {k:"" for k in fields}

    def save(self, commit=True):
        instance = super().save(commit)
        denuncias= self.cleaned_data['denuncias']
        for denuncia in denuncias:
            denuncia.actualizar_creacion()
            denuncia.asignada = "Si"
            denuncia.save()
            instance.denuncia_set.add(denuncia)
        return instance

class DenunciaForm(forms.ModelForm):
    texto = forms.CharField(label="Descripción de la denuncia",widget=forms.Textarea(attrs={'class':'textarea','rows':2,'placeholder':'Descripción de la denuncia'}))
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'input','placeholder':'Nombre del denunciante'}))
    apellidos = forms.CharField(widget=forms.TextInput(attrs={'class':'input','placeholder':'Apellidos del denunciante'}))
    fecha = forms.DateField(input_formats=['%d/%m/%y','%y-%m-%d'],widget=forms.DateInput(attrs={'class':'input','placeholder':'Fecha del hecho. Ejemplo: 17/1/21'}))
    hora = forms.TimeField(input_formats=['%H:%M','%H:%M:%S'],widget=forms.TimeInput(attrs={'class':'input','placeholder':'Hora del hecho. Ejemplo: 23:00'}))
    area = forms.CharField(label="Área",widget=forms.TextInput(attrs={'class':'input','placeholder':'Área del hecho'}))
    usuario_d = forms.CharField(label="Usuario denunciado",widget=forms.TextInput(attrs={'class':'input','placeholder':'Usuario de la persona denunciada'}))
    usuario = forms.ModelChoiceField(label="Usuario del denunciante",queryset=User.objects.all())

    class Meta:
        model = denuncia
        fields = ['nombre','apellidos','fecha','hora','area','usuario_d','usuario','texto']
        help_texts = {k:"" for k in fields}

class ComisionForm(forms.ModelForm):
    presidente = forms.ModelChoiceField(label="Usuario del presidente",queryset=User.objects.all())
    secretario = forms.ModelChoiceField(label="Usuario del secretario",queryset=User.objects.all())
    p_guia = forms.ModelChoiceField(label="Usuario del profesor guia",queryset=User.objects.all())
    v_feu = forms.ModelChoiceField(label="Usuario del vocal feu",queryset=User.objects.all())
    otros = forms.CharField(label="Otros",widget=forms.TextInput(attrs={'class':'input','placeholder':'Usuarios de otras personas involucradas'}))
    denuncias = forms.ModelMultipleChoiceField(queryset=denuncia.objects.all(),widget=forms.CheckboxSelectMultiple())
    
    class Meta:
        model = comision
        fields = ['presidente','secretario','p_guia','v_feu','otros','denuncias']
        help_texts = {k:"" for k in fields}
    
    def save(self, commit=True):
        instance = super().save(commit)
        denuncias= self.cleaned_data['denuncias']
        for denuncia in denuncias:
            denuncia.actualizar_creacion()
            denuncia.asignada = "Si"
            denuncia.save()
            instance.denuncia_set.add(denuncia)
        return instance