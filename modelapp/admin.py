from django.contrib import admin
from modelapp.models import caballo
from modelapp.form import formcaballo
from django import forms
class CaballoAdmin(admin.ModelAdmin):
    form = formcaballo

    def save_model(self, request, obj, form, change):
        # Validaciones antes de guardar el modelo
        if len(obj.nombre) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
        if not obj.raza.isalpha():
            raise forms.ValidationError("La raza solo puede contener letras.")
        if len(obj.color) < 3:
            raise forms.ValidationError("El color debe tener al menos 3 caracteres.")

        super().save_model(request, obj, form, change)

admin.site.register(caballo, CaballoAdmin)