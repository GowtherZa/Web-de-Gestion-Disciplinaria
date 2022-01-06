from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import perfil

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

# class UserRegisterForm(UserCreationForm):
#     nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
#     apellidos = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
#     correo = forms.EmailField(widget=forms.EmailInput(attrs={'class':'input'}))
#     cat_docente = forms.ChoiceField(choices=cat_docentes,widget=forms.Select(attrs={'class':' '}))
#     rol = forms.ChoiceField(choices=roles,widget=forms.Select(attrs={'class':''}))
#     cargo = forms.ChoiceField(choices=cargos,widget=forms.Select(attrs={'class':''}))
    
#     class Meta:
#         model = User
#         fields = ['username','password1','password2','nombre','apellidos','correo','cat_docente','rol','cargo']
#         help_texts = {k:"" for k in fields}
     

#     def __init__(self,*args,**kwargs):
#         super(UserCreationForm,self).__init__(*args,**kwargs)

#         self.fields['username'].widget.attrs['class'] = 'input'
#         self.fields['password1'].widget.attrs['class'] = 'input'
#         self.fields['password2'].widget.attrs['class'] = 'input'

#         self.fields['username'].label= 'Usuario'
#         self.fields['password1'].label = 'Contraseña'
#         self.fields['password2'].label = 'Confirmar contraseña'



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