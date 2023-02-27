from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from .models import CustomUser

class RegisterForm(UserCreationForm, ModelForm):
            
    error_messages = {
        'password_mismatch': _('Las contraseñas no coinciden'),
    }

    password1 = forms.CharField(
        label='',
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'placeholder': 'Contraseña',
            }),
        error_messages={
            'required': 'Este campo debe ser rellenado',
        },
    )

    password2 = forms.CharField(
        label='',
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'placeholder': 'Repita la contraseña',
            }),
        error_messages={
            'required': 'Este campo debe ser rellenado',
        },
    )

    class Meta():
        model = CustomUser

        fields = [
            'username',
            'email',
        ]
        
        labels = {
            'username': '',
            'email': '',
        }

        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Nombre de Usuario',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email',
            }),
        }
