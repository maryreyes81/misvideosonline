# --------------------------
# AVANCE 3.PY (Django + PostgreSQL)
# Guarda en BD Pro_Gol usando modelos:
#   TBL_Usuario, TBL_Video, TBL_UsuarioVideo
# --------------------------

import re
from typing import Any

# ---- Django setup ----
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from videos_app.models import TBL_Usuario, TBL_Video, TBL_UsuarioVideo


# --------------------------
# MENSAJES DE VALIDACIÓN
# --------------------------
def mostrar_mensaje_validacion(campo: str, tipo_error: str) -> None:
    if campo == "nomina":
        print("Nómina inválida. Solo letras y números.")
    elif campo == "nombre":
        print("Nombre inválido. Solo letras y espacios.")
    elif campo == "cantidad":
        print("Cantidad inválida. Solo números.")
    elif campo == "titulo":
        print("Título inválido. Letras, números y espacios.")
    elif campo == "nombre_video":
        print("Nombre del video inválido. Letras, números y espacios.")
    elif campo == "extension":
        print("Extensión inválida. Solo letras y números.")
    elif campo == "tamano" and tipo_error == "solo_numeros":
        print("Tamaño inválido. Solo números.")
    elif campo == "tamano" and tipo_error == "rango":
        print("El archivo no debe pesar más de 3 MB.")
    else:
        print("Entrada inválida.")


# --------------------------
# VALIDACIONES
# --------------------------
def es_alfanumerico(valor: str) -> bool:
    return bool(re.fullmatch(r"[A-Za-z0-9]+", valor))


def es_alfanumerico_con_espacios(valor: str) -> bool:
    return bool(re.fullmatch(r"[A-Za-z0-9 ]+", valor)) and valor.strip() != ""


def es_alfabetico(valor: str) -> bool:
    return bool(re.fullmatch(r"[A-Za-z ]+", valor)) and valor.strip() != ""


def es_numerico(valor: str) -> bool:
    return bool(re.fullmatch(r"[0-9]+", valor))


# --------------------------
# MANEJO DE EXCEPCIONES
# --------------------------
def ejecutar_con_excepciones(funcion, *args: Any, **kwargs: Any) -> Any:
    try:
        return funcion(*args, **kwargs)
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        raise


# --------------------------
# CLASE PERSONA
# --------------------------
class Persona:
    def __init__(self) -> None:
        self.nombre: str = ""
        self.nomina: str = ""

    def capturar_nombre(self) -> None:
        while True:
            nombre = input("Captura tu nombre (solo letras): ").strip()
            if es_alfabetico(nombre) and len(nombre) <= 50:
                self.nombre = nombre
                return
            mostrar_mensaje_validacion("nombre", "formato")

    def capturar_id(self) -> None:
        while True:
            nomina = input("Captura tu número de nómina (alfanumérico): ").strip()
            if es_alfanumerico(nomina) and len(nomina) <= 10:
                self.nomina = nomina
                return
            mostrar_mensaje_validacion("nomina", "formato")


# --------------------------
# CLASE VIDEOS
# --------------------------
class Videos:
    def __init__(self) -> None:
        self.nombre_video: str = ""
        self.extension: str = ""
        self.tamano: int = 0

    # ACEPTA ESPACIOS, GUARDA SIN ESPACIOS
    def capturar_nombre_video(self) -> None:
        while True:
            nombre_video = input(
                "Nombre del video (alfanumérico y espacios): "
            ).strip()

            if es_alfanumerico_con_espacios(nombre_video) and len(nombre_video) <= 50:
                self.nombre_video = nombre_video.replace(" ", "")
                return

            mostrar_mensaje_validacion("nombre_video", "formato")

    def capturar_extension(self) -> None:
        while True:
            extension = input("Extensión del video (ej: mpg, mov): ").strip().lower()
            if es_alfanumerico(extension) and len(extension) <= 5:
                self.extension = extension
                return
            mostrar_mensaje_validacion("extension", "formato")

    def capturar_tamano(self) -> None:
        while True:
            tamano_str = input("Tamaño del video (0 a 3 MB): ").strip()

            if not es_numerico(tamano_str):
                mostrar_mensaje_validacion("tamano", "solo_numeros")
                continue

            tamano = int(tamano_str)

            if tamano < 0 or tamano > 3:
                mostrar_mensaje_validacion("tamano", "rango")
                continue

            self.tamano = tamano
            return

    def imprimir_datos(self) -> None:
        print(f"Nombre del video (guardado): {self.nombre_video}")
        print(f"Extensión: {self.extension}")
        print(f"Tamaño (MB): {self.tamano}")


# --------------------------
# CAPTURAS GENERALES
# --------------------------
def capturar_cantidad_videos() -> int:
    while True:
        cantidad = input("¿Cuántos videos deseas subir?: ").strip()
        if es_numerico(cantidad) and int(cantidad) > 0:
            return int(cantidad)
        mostrar_mensaje_validacion("cantidad", "formato")


def capturar_titulo_video() -> str:
    while True:
        titulo = input("Título del video (alfanumérico y espacios): ").strip()
        if es_alfanumerico_con_espacios(titulo) and len(titulo) <= 50:
            return titulo
        mostrar_mensaje_validacion("titulo", "formato")


# --------------------------
# GUARDAR EN BD
# --------------------------
def guardar_en_bd(persona: Persona, videos: list[dict[str, Any]]) -> None:
    usuario, _ = TBL_Usuario.objects.get_or_create(
        nomina=persona.nomina,
        defaults={"nombre": persona.nombre},
    )

    if usuario.nombre != persona.nombre:
        usuario.nombre = persona.nombre
        usuario.save()

    for v in videos:
        video = TBL_Video.objects.create(
            nombre_video=v["nombre_video"],
            extension=v["extension"],
            tamano=v["tamano"],
        )
        TBL_UsuarioVideo.objects.create(usuario=usuario, video=video)


# --------------------------
# MAIN
# --------------------------
def main() -> None:
    persona = Persona()
    persona.capturar_id()
    persona.capturar_nombre()

    cantidad = capturar_cantidad_videos()

    confirmar = input(
        f"Bienvenido {persona.nombre}, tu nómina es {persona.nomina} "
        f"y subirás {cantidad} videos. ¿Es correcto? Sí/No: "
    ).strip().lower()

    if confirmar not in ("si", "sí", "s"):
        print("Proceso cancelado.")
        return

    lista_videos: list[dict[str, Any]] = []

    for i in range(1, cantidad + 1):
        print(f"\n--- Video {i} ---")

        titulo = capturar_titulo_video()

        video = Videos()
        video.capturar_nombre_video()
        video.capturar_extension()
        video.capturar_tamano()
        video.imprimir_datos()

        lista_videos.append({
            "titulo": titulo,  # NO se guarda (no existe columna)
            "nombre_video": video.nombre_video,
            "extension": video.extension,
            "tamano": video.tamano,
        })

    guardar_en_bd(persona, lista_videos)
    print("\n✅ Información guardada correctamente en Pro_Gol")


if __name__ == "__main__":
    ejecutar_con_excepciones(main)


