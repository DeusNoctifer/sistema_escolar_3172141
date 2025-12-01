from django import forms
from django.forms import TextInput, Select, EmailInput, FileInput, PasswordInput


# Formulario para el registro de Usuarios
class RegistroUsuarioFrm(forms.ModelForm):
    clave = forms.CharField(
        label = "Contraseña",
        widget = PasswordInput(),
        help_text = "Debe tener al menos 8 caracteres, incluir una mayúscula, una minúscula, un dígito y un caracter especial(#$%!*/_).",
    )

    confirmar_clave = forms.CharField(
        label = "Confirmar Contraseña",
        widget = PasswordInput()
    )

    class Meta:
        model = Usuarios
        fields = ['correo', 'rol', 'tipo_documento', 'documento', 'clave']

