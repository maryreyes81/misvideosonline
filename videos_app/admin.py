from django.contrib import admin
from .models import TBL_Usuario, TBL_Video, TBL_UsuarioVideo

@admin.register(TBL_Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("id", "nomina", "nombre")
    search_fields = ("nomina", "nombre")

@admin.register(TBL_Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre_video", "extension", "tamano")
    search_fields = ("nombre_video", "extension")
    list_filter = ("extension",)

@admin.register(TBL_UsuarioVideo)
class UsuarioVideoAdmin(admin.ModelAdmin):
    list_display = ("id", "usuario", "video")
    search_fields = ("usuario__nomina", "usuario__nombre", "video__nombre_video")
