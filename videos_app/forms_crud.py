from django import forms
from .models import TBL_Video

class VideoModelForm(forms.ModelForm):
    class Meta:
        model = TBL_Video
        fields = ["nombre_video", "extension", "tamano"]

    def clean_nombre_video(self):
        v = (self.cleaned_data.get("nombre_video") or "").strip()
        # acepta espacios al capturar, guarda sin espacios
        v = v.replace(" ", "")
        if not v:
            raise forms.ValidationError("Nombre del video requerido.")
        return v

    def clean_extension(self):
        v = (self.cleaned_data.get("extension") or "").strip().lower()
        if not v.isalnum():
            raise forms.ValidationError("Extensión inválida. Solo letras y números.")
        return v

    def clean_tamano(self):
        t = self.cleaned_data.get("tamano")
        if t is None:
            raise forms.ValidationError("Tamaño requerido.")
        if t < 0 or t > 3:
            raise forms.ValidationError("El archivo no debe pesar más de 3 MB.")
        return t
