# Importa expresiones regulares para validar texto
import re

# Importa Any para documentar retornos (opcional)
from typing import Any


# --------------------------
# FUNCIÓN ÚNICA DE MENSAJES
# --------------------------
def mostrar_mensaje_validacion(campo: str, tipo_error: str) -> None:
    # Muestra mensaje para nómina con formato incorrecto
    if campo == "nomina" and tipo_error == "formato":
        print('Nómina en formato incorrecto. Debe capturar solo números y letras.')
    # Muestra mensaje para nombre de usuario con formato incorrecto
    elif campo == "nombre" and tipo_error == "formato":
        print('Nombre de usuario en formato incorrecto. Debe capturar solo letras.')
    # Muestra mensaje para cantidad de videos con formato incorrecto
    elif campo == "cantidad" and tipo_error == "formato":
        print('Cantidad de videos en formato incorrecto. Debe capturar solo números.')
    # Muestra mensaje para título con formato incorrecto
    elif campo == "titulo" and tipo_error == "formato":
        print('Título del video en formato incorrecto. Debe capturar solo números y letras.')
    # Muestra mensaje para nombre del video con formato incorrecto
    elif campo == "nombre_video" and tipo_error == "formato":
        print('Nombre del video en formato incorrecto. Debe capturar solo números y letras.')
    # Muestra mensaje para extensión con formato incorrecto
    elif campo == "extension" and tipo_error == "formato":
        print('Extensión del video en formato incorrecto. Debe capturar solo números y letras.')
    # Muestra mensaje si tamaño no es numérico
    elif campo == "tamano" and tipo_error == "solo_numeros":
        print('Tamaño del video en formato incorrecto. Debe capturar solo números')
    # Muestra mensaje si tamaño está fuera de 0 a 3
    elif campo == "tamano" and tipo_error == "rango":
        print('El archivo no debe pesar más de 3 M')
    # Mensaje genérico por seguridad
    else:
        print("Entrada inválida.")


# --------------------------
# VALIDACIONES
# --------------------------
def es_alfanumerico(valor: str) -> bool:
    # Valida que el texto contenga solo letras y números
    return bool(re.fullmatch(r"[A-Za-z0-9]+", valor))


def es_alfabetico(valor: str) -> bool:
    # Valida que el texto contenga solo letras y espacios, y que no esté vacío
    return bool(re.fullmatch(r"[A-Za-z ]+", valor)) and valor.strip() != ""


def es_numerico(valor: str) -> bool:
    # Valida que el texto contenga solo números
    return bool(re.fullmatch(r"[0-9]+", valor))


# --------------------------
# EXCEPCIONES
# --------------------------
def ejecutar_con_excepciones(funcion, *args: Any, **kwargs: Any) -> Any:
    # Ejecuta una función y captura errores inesperados
    try:
        return funcion(*args, **kwargs)
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        raise


# --------------------------
# CLASE PERSONA
# --------------------------
class Persona:
    # Constructor: inicializa atributos nombre y nómina
    def __init__(self) -> None:
        self.nombre: str = ""
        self.nomina: str = ""

    # Captura el nombre del usuario con validación
    def capturar_nombre(self) -> None:
        while True:
            nombre = input("Captura tu nombre (solo letras): ").strip()
            if es_alfabetico(nombre):
                self.nombre = nombre
                return
            mostrar_mensaje_validacion("nombre", "formato")

    # Captura la nómina del usuario con validación
    def capturar_id(self) -> None:
        while True:
            nomina = input("Captura tu número de nómina (alfanumérico): ").strip()
            if es_alfanumerico(nomina):
                self.nomina = nomina
                return
            mostrar_mensaje_validacion("nomina", "formato")

    # Imprime el nombre del usuario
    def imprimir_nombre(self) -> None:
        print(f"Nombre: {self.nombre}")

    # Imprime la nómina del usuario
    def imprimir_id(self) -> None:
        print(f"Nómina: {self.nomina}")


# --------------------------
# CLASE VIDEOS
# --------------------------
class Videos:
    # Constructor: inicializa atributos del video
    def __init__(self) -> None:
        self.nombre_video: str = ""
        self.extension: str = ""
        self.tamano: int = 0

    # Captura el nombre del video con validación
    def capturar_nombre_video(self) -> None:
        while True:
            nombre_video = input("Nombre del video (alfanumérico): ").strip()
            if es_alfanumerico(nombre_video):
                self.nombre_video = nombre_video
                return
            mostrar_mensaje_validacion("nombre_video", "formato")

    # Captura la extensión del video con validación
    def capturar_extension(self) -> None:
        while True:
            extension = input("Extensión del video (alfanumérico, ej: mpg, mov): ").strip()
            if es_alfanumerico(extension):
                self.extension = extension
                return
            mostrar_mensaje_validacion("extension", "formato")

    # Captura el tamaño del video con validación (0 a 3)
    def capturar_tamano(self) -> None:
        while True:
            tamano_str = input("Tamaño del video (0 a 3 megas): ").strip()
            if not es_numerico(tamano_str):
                mostrar_mensaje_validacion("tamano", "solo_numeros")
                continue
            tamano = int(tamano_str)
            if tamano < 0 or tamano > 3:
                mostrar_mensaje_validacion("tamano", "rango")
                continue
            self.tamano = tamano
            return

    # Imprime el nombre del video
    def imprimir_nombre_video(self) -> None:
        print(f"Nombre del video: {self.nombre_video}")

    # Imprime la extensión del video
    def imprimir_extension(self) -> None:
        print(f"Extensión: {self.extension}")

    # Imprime el tamaño del video
    def imprimir_tamano(self) -> None:
        print(f"Tamaño (MB): {self.tamano}")


# --------------------------
# CAPTURA DE DATOS GENERALES
# (Cantidad de videos + Títulos)
# --------------------------
def capturar_cantidad_videos() -> int:
    # Captura cuántos videos desea subir el usuario
    while True:
        cantidad_str = input("¿Cuántos videos deseas subir? (solo números): ").strip()
        if es_numerico(cantidad_str):
            return int(cantidad_str)
        mostrar_mensaje_validacion("cantidad", "formato")


def capturar_titulo_video() -> str:
    # Captura el título del video con validación alfanumérica
    while True:
        titulo = input("Título del video (alfanumérico): ").strip()
        if es_alfanumerico(titulo):
            return titulo
        mostrar_mensaje_validacion("titulo", "formato")


# --------------------------
# GUARDADO EN salida.txt
# --------------------------
def guardar_salida(persona: Persona, cantidad: int, lista_videos: list[dict[str, Any]]) -> None:
    # Crea lista de campos con nómina, nombre y cantidad
    campos: list[str] = [persona.nomina, persona.nombre, str(cantidad)]

    # Agrega campos de cada video en el orden solicitado
    for v in lista_videos:
        campos.extend([
            v["titulo"],
            v["nombre_video"],
            v["extension"],
            str(v["tamano"])
        ])

    # Une campos con separador " | "
    linea = " | ".join(campos)

    # Guarda en salida.txt en modo append
    with open("salida.txt", "a", encoding="utf-8") as archivo:
        archivo.write(linea + "\n")


# --------------------------
# MAIN (MISMA LÓGICA DE ETAPA 1)
# --------------------------
def main() -> None:
    # Bucle principal para poder reintentar si la info no es correcta
    while True:
        # Crea un objeto Persona
        persona = Persona()

        # Captura la nómina usando el objeto Persona
        persona.capturar_id()

        # Captura el nombre usando el objeto Persona
        persona.capturar_nombre()

        # Captura la cantidad de videos
        cantidad = capturar_cantidad_videos()

        # Mensaje de confirmación solicitado
        respuesta = input(
            f"Bienvenido {persona.nombre}, tu número de nómina es {persona.nomina} y estás intentando subir "
            f"{cantidad} videos. ¿Es correcta la información? Sí/No: "
        ).strip().lower()

        # Si la respuesta es Sí, se capturan los videos
        if respuesta in ("si", "sí", "s"):
            # Lista para almacenar los videos capturados
            lista_videos: list[dict[str, Any]] = []

            # Ciclo para capturar cada video
            for i in range(1, cantidad + 1):
                print(f"\n--- Captura de datos del video {i} ---")

                # Captura el título (no está en la clase Videos por requisitos, se captura aparte)
                titulo = capturar_titulo_video()

                # Crea un objeto Videos para este video
                video = Videos()

                # Captura datos del video usando el objeto Videos
                video.capturar_nombre_video()
                video.capturar_extension()
                video.capturar_tamano()

                # (Opcional) Imprime lo capturado para evidencia en pantalla
                video.imprimir_nombre_video()
                video.imprimir_extension()
                video.imprimir_tamano()

                # Agrega a la lista el video como diccionario para guardarlo en archivo
                lista_videos.append({
                    "titulo": titulo,
                    "nombre_video": video.nombre_video,
                    "extension": video.extension,
                    "tamano": video.tamano
                })

            # Guarda la salida en archivo
            guardar_salida(persona, cantidad, lista_videos)

            # Mensaje final de confirmación
            print("\n✅ Información guardada correctamente en salida.txt")
            return

        # Si la respuesta es No, pregunta si desea salir
        if respuesta in ("no", "n"):
            salir = input("¿Deseas salir del sistema? Sí/No: ").strip().lower()

            # Si quiere salir, muestra mensaje y termina
            if salir in ("si", "sí", "s"):
                print("Muchas gracias por haber usado nuestro sistema, hasta pronto.")
                return

            # Si no quiere salir, reinicia el proceso
            if salir in ("no", "n"):
                print("\n🔁 Perfecto, capturemos nuevamente tus datos.\n")
                continue

        # Si escribe algo distinto a Sí/No, vuelve a pedir todo
        print("\nEntrada no válida. Debes contestar Sí o No.\n")


# Punto de entrada del programa
if __name__ == "__main__":
    # Ejecuta main dentro del manejador de excepciones
    ejecutar_con_excepciones(main)
