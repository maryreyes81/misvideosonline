from django import forms
from django.forms import formset_factory
import re

def es_alfanumerico(s: str) -> bool:
    return bool(re.fullmatch(r"[A-Za-z0-9]+", s))

def es_alfanumerico_con_espacios(s: str) -> bool:
    return bool(re.fullmatch(r"[A-Za-z0-9 ]+", s)) and s.strip() != ""

def es_alfabetico(s: str) -> bool:
    return bool(re.fullmatch(r"[A-Za-z ]+", s)) and s.strip() != ""


class UsuarioCantidadForm(forms.Form):
    nomina = forms.CharField(max_length=10, label="Número de nómina")
    nombre = forms.CharField(max_length=50, label="Nombre completo")
    cantidad = forms.IntegerField(min_value=1, max_value=100, label="Cantidad de videos")

    def clean_nomina(self):
        v = self.cleaned_data["nomina"].strip()
        if not es_alfanumerico(v):
            raise forms.ValidationError("Nómina inválida. Solo letras y números.")
        return v

    def clean_nombre(self):
        v = self.cleaned_data["nombre"].strip()
        if not es_alfabetico(v):
            raise forms.ValidationError("Nombre inválido. Solo letras y espacios.")
        return v

class VideoForm(forms.Form):
    titulo = forms.CharField(max_length=50, label="Título del video")
    nombre_video = forms.CharField(max_length=50, label="Nombre del video")
    extension = forms.CharField(max_length=5, label="Extensión (mpg, mov...)")
    tamano = forms.IntegerField(min_value=0, max_value=3, label="Tamaño (MB)")

    def clean_titulo(self):
        v = self.cleaned_data["titulo"].strip()
        if not es_alfanumerico_con_espacios(v):
            raise forms.ValidationError("Título inválido. Letras, números y espacios.")
        return v

    def clean_nombre_video(self):
        """
        ✅ Para tu caso: ACEPTA ESPACIOS al capturar,
        pero se guarda como “archivo” sin espacios.
        """
        v = self.cleaned_data["nombre_video"].strip()
        if not es_alfanumerico_con_espacios(v):
            raise forms.ValidationError("Nombre inválido. Letras, números y espacios.")
        return v.replace(" ", "")  # se guarda sin espacios

    def clean_extension(self):
        v = self.cleaned_data["extension"].strip().lower()
        if not es_alfanumerico(v):
            raise forms.ValidationError("Extensión inválida. Solo letras y números.")
        return v


VideoFormSet = formset_factory(VideoForm, extra=0, min_num=1, validate_min=True)
