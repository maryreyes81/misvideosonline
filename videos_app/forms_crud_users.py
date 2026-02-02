from django import forms
from .models import TBL_Usuario, TBL_UsuarioVideo

class UsuarioModelForm(forms.ModelForm):
    class Meta:
        model = TBL_Usuario
        fields = ["nomina", "nombre"]

    def clean_nomina(self):
        v = (self.cleaned_data.get("nomina") or "").strip()
        if not v.isalnum():
            raise forms.ValidationError("Nómina inválida. Solo letras y números.")
        return v

    def clean_nombre(self):
        v = (self.cleaned_data.get("nombre") or "").strip()
        # Permite espacios, pero solo letras/espacios
        for ch in v:
            if not (ch.isalpha() or ch == " "):
                raise forms.ValidationError("Nombre inválido. Solo letras y espacios.")
        if not v:
            raise forms.ValidationError("Nombre requerido.")
        return v


class UsuarioVideoModelForm(forms.ModelForm):
    class Meta:
        model = TBL_UsuarioVideo
        fields = ["usuario", "video"]
