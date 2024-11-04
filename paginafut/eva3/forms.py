from django import forms
from .models import Partido,Comentario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PartidoForm(forms.ModelForm):
    class Meta:
        model = Partido
        fields = '__all__'
        widgets = {
            'fecha': forms.SelectDateWidget(),
            'horapartido': forms.TimeInput(attrs={'type': 'time'}) 
        }

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','password1','password2']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'