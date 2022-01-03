from django import forms
from django.contrib.auth.forms import UserCreationForm
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

class UserRegisterForm(UserCreationForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    apellidos = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    correo = forms.EmailField(widget=forms.EmailInput(attrs={'class':'input'}))
    cat_docente = forms.ChoiceField(choices=cat_docentes,widget=forms.Select(attrs={'class':' '}))
    rol = forms.ChoiceField(choices=roles,widget=forms.Select(attrs={'class':''}))
    cargo = forms.ChoiceField(choices=cargos,widget=forms.Select(attrs={'class':''}))
    
    class Meta:
        model = User
        fields = ['username','password1','password2','nombre','apellidos','correo','cat_docente','rol','cargo']
        help_texts = {k:"" for k in fields}
     

    def __init__(self,*args,**kwargs):
        super(UserCreationForm,self).__init__(*args,**kwargs)

        self.fields['username'].widget.attrs['class'] = 'input'
        self.fields['password1'].widget.attrs['class'] = 'input'
        self.fields['password2'].widget.attrs['class'] = 'input'

        self.fields['username'].label= 'Usuario'
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Confirmar contraseña'
