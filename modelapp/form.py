from django import forms
from modelapp.models import caballo
import re
class formcaballo (forms.ModelForm):
    class Meta:
        model=caballo
        fields='__all__'

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
        if not re.match("^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$", nombre):
            raise forms.ValidationError("El nombre solo debe contener letras.")
        return nombre

    def clean_raza(self):
        raza = self.cleaned_data.get('raza')
        if len(raza) < 3:
            raise forms.ValidationError("La raza debe tener al menos 3 caracteres.")
        if not re.match("^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$", raza):
            raise forms.ValidationError("La raza solo debe contener letras.")
        return raza

    def clean_color(self):
        color = self.cleaned_data.get('color')
        if len(color) < 3:
            raise forms.ValidationError("El color debe tener al menos 3 caracteres.")
        if not re.match("^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$", color):
            raise forms.ValidationError("El color solo debe contener letras.")
        return color   