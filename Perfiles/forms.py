from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from Perfiles.models import Perfil 
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserForm(UserCreationForm):
    username = forms.CharField(max_length=10)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User 
        fields = ("username", "email", "password1", "password2" )
        labels = {
		'username':'Usuario',
		'email':'Correo',
		'password1':'Contraseña'
		}

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Perfil 
        fields = ("numero_carnet", "cui", "profesion")
        labels = {
		'numero_carnet':'Número de carnet',
		'profesion':'Profesión'
		}


class EditUserForm(UserChangeForm):
    username = forms.CharField(label='Usuario', help_text= " ")
    password = ReadOnlyPasswordHashField(label='Contraseña', help_text= "")
    class Meta:
        model = User
        fields = ("username", "email")
    


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ("numero_carnet", "cui", "profesion")