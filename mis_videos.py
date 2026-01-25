# Importa expresiones regulares para validar texto (alfanumérico, alfabético, numérico).
import re

# Importa el tipo Any para documentar retornos (opcional).
from typing import Any


# Función única para mostrar mensajes de validación (deberá ser una sola función).
def mostrar_mensaje_validacion(campo: str, tipo_error: str) -> None:
    # Si el campo es nómina y el formato es incorrecto, imprime el mensaje requerido.
    if campo == "nomina" and tipo_error == "formato":
        print('Nómina en formato incorrecto. Debe capturar solo números y letras.')
    # Si el campo es nombre y el formato es incorrecto, imprime el mensaje requerido.
    elif campo == "nombre" and tipo_error == "formato":
        print('Nombre de usuario en formato incorrecto. Debe capturar solo letras.')
    # Si el campo es cantidad y el formato es incorrecto, imprime el mensaje requerido.
    elif campo == "cantidad" and tipo_error == "formato":
        print('Cantidad de videos en formato incorrecto. Debe capturar solo números.')
    # Si el campo es título y el formato es incorrecto, imprime el mensaje requerido.
    elif campo == "titulo" and tipo_error == "formato":
        print('Título del video en formato incorrecto. Debe capturar solo números y letras.')
    # Si el campo es nombre_video y el formato es incorrecto, imprime el mensaje requerido.
    elif campo == "nombre_video" and tipo_error == "formato":
        print('Nombre del video en formato incorrecto. Debe capturar solo números y letras.')
    # Si el campo es extension y el formato es incorrecto, imprime el mensaje requerido.
    elif campo == "extension" and tipo_error == "formato":
        print('Extensión del video en formato incorrecto. Debe capturar solo números y letras.')
    # Si el campo es tamano y el error es que metió letras, imprime el mensaje requerido.
    elif campo == "tamano" and tipo_error == "solo_numeros":
        print('Tamaño del video en formato incorrecto. Debe capturar solo números')
    # Si el campo es tamano y el error es que se salió del rango 0-3, imprime el mensaje requerido.
    elif campo == "tamano" and tipo_error == "rango":
        print('El archivo no debe pesar más de 3 M')
    # Si llega un caso no contemplado, muestra un mensaje genérico (por seguridad).
    else:
        print("Entrada inválida.")


# Función (o funciones) para validar capturas del usuario: alfanumérico (A-Z, a-z, 0-9).
def es_alfanumerico(valor: str) -> bool:
    # Verifica con regex que tenga al menos 1 caracter y que sean solo letras o números.
    return bool(re.fullmatch(r"[A-Za-z0-9]+", valor))


# Función para validar capturas del usuario: alfabético (A-Z, a-z).
def es_alfabetico(valor: str) -> bool:
    # Verifica con regex que tenga al menos 1 caracter y que sean solo letras y espacios.
    return bool(re.fullmatch(r"[A-Za-z ]+", valor)) and valor.strip() != ""


# Función para validar capturas del usuario: numérico (0-9).
def es_numerico(valor: str) -> bool:
    # Verifica con regex que tenga al menos 1 dígito y que sean solo números.
    return bool(re.fullmatch(r"[0-9]+", valor))


# Función para manejo de excepciones: ejecuta una función y captura errores controlados.
def ejecutar_con_excepciones(funcion, *args: Any, **kwargs: Any) -> Any:
    # Intenta ejecutar la función.
    try:
        return funcion(*args, **kwargs)
    # Si ocurre cualquier excepción, muestra el error y vuelve a lanzar (para debug/seguridad).
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        raise


# Función para pedir id, nombre y cantidad de videos al usuario (con validaciones).
def pedir_datos_usuario() -> tuple[str, str, int]:
    # Bucle para pedir nómina hasta que sea válida.
    while True:
        # Solicita al usuario su id (número de nómina) como texto.
        nomina = input("Captura tu número de nómina (alfanumérico): ").strip()
        # Valida que sea alfanumérico.
        if es_alfanumerico(nomina):
            # Si es válido, rompe el bucle.
            break
        # Si no es válido, muestra el mensaje requerido.
        mostrar_mensaje_validacion("nomina", "formato")

    # Bucle para pedir nombre hasta que sea válido.
    while True:
        # Solicita al usuario su nombre como texto.
        nombre = input("Captura tu nombre (solo letras): ").strip()
        # Valida que sea alfabético (permitiendo espacios).
        if es_alfabetico(nombre):
            # Si es válido, rompe el bucle.
            break
        # Si no es válido, muestra el mensaje requerido.
        mostrar_mensaje_validacion("nombre", "formato")

    # Bucle para pedir cantidad de videos hasta que sea válida.
    while True:
        # Solicita cuántos videos subirá.
        cantidad_str = input("¿Cuántos videos deseas subir? (solo números): ").strip()
        # Valida que sea numérico.
        if es_numerico(cantidad_str):
            # Convierte a entero.
            cantidad = int(cantidad_str)
            # Si es válido, rompe el bucle.
            break
        # Si no es válido, muestra el mensaje requerido.
        mostrar_mensaje_validacion("cantidad", "formato")

    # Regresa los datos capturados (nómina y nombre como str, cantidad como int).
    return nomina, nombre, cantidad


# Función para capturar título, nombre, extensión y megas de cada uno de los videos a subir.
def capturar_videos(cantidad: int) -> list[dict[str, Any]]:
    # Crea una lista vacía para almacenar los videos.
    videos: list[dict[str, Any]] = []
    # Repite el proceso para cada video según la cantidad indicada.
    for i in range(1, cantidad + 1):
        # Imprime un encabezado indicando qué video se está capturando.
        print(f"\n--- Captura de datos del video {i} ---")

        # Bucle para pedir título hasta que sea válido (alfanumérico).
        while True:
            # Solicita título del video.
            titulo = input("Título del video (alfanumérico): ").strip()
            # Valida alfanumérico.
            if es_alfanumerico(titulo):
                # Si es válido, rompe el bucle.
                break
            # Si no es válido, muestra el mensaje requerido.
            mostrar_mensaje_validacion("titulo", "formato")

        # Bucle para pedir nombre del video hasta que sea válido (alfanumérico).
        while True:
            # Solicita nombre del video.
            nombre_video = input("Nombre del video (alfanumérico): ").strip()
            # Valida alfanumérico.
            if es_alfanumerico(nombre_video):
                # Si es válido, rompe el bucle.
                break
            # Si no es válido, muestra el mensaje requerido.
            mostrar_mensaje_validacion("nombre_video", "formato")

        # Bucle para pedir extensión del video hasta que sea válida (alfanumérico).
        while True:
            # Solicita extensión del video (sin forzar el punto).
            extension = input("Extensión del video (alfanumérico, ej: mpg, mov): ").strip()
            # Valida alfanumérico (si quieres permitir el punto, dímelo y lo ajusto).
            if es_alfanumerico(extension):
                # Si es válido, rompe el bucle.
                break
            # Si no es válido, muestra el mensaje requerido.
            mostrar_mensaje_validacion("extension", "formato")

        # Bucle para pedir tamaño hasta que sea válido: numérico y entre 0 y 3.
        while True:
            # Solicita tamaño del video en megas.
            tamano_str = input("Tamaño del video (0 a 3 megas): ").strip()
            # Si no es numérico, muestra el mensaje requerido para alfanumérico.
            if not es_numerico(tamano_str):
                mostrar_mensaje_validacion("tamano", "solo_numeros")
                continue
            # Convierte a entero.
            tamano = int(tamano_str)
            # Si está fuera de rango, muestra el mensaje requerido.
            if tamano < 0 or tamano > 3:
                mostrar_mensaje_validacion("tamano", "rango")
                continue
            # Si todo está bien, rompe el bucle.
            break

        # Agrega el video capturado a la lista.
        videos.append(
            {
                "titulo": titulo,
                "nombre_video": nombre_video,
                "extension": extension,
                "tamano": tamano,
            }
        )

    # Regresa la lista de videos capturados.
    return videos


# Función para guardar la información validada en salida.txt con el formato solicitado.
def guardar_salida(nomina: str, nombre: str, cantidad: int, videos: list[dict[str, Any]]) -> None:
    # Construye una lista de campos en el orden requerido.
    campos: list[str] = []
    # Agrega nómina, nombre y cantidad.
    campos.append(nomina)
    campos.append(nombre)
    campos.append(str(cantidad))
    # Recorre cada video y agrega sus datos al formato.
    for v in videos:
        campos.append(v["titulo"])
        campos.append(v["nombre_video"])
        campos.append(v["extension"])
        campos.append(str(v["tamano"]))
    # Une todos los campos con " | " como separador.
    linea = " | ".join(campos)
    # Abre (o crea) el archivo salida.txt en modo append para agregar una línea por ejecución.
    with open("salida.txt", "a", encoding="utf-8") as f:
        # Escribe la línea y salto de línea.
        f.write(linea + "\n")


# Función principal que controla el flujo y condicionales Sí/No y salida del sistema.
def main() -> None:
    # Bucle principal para permitir reintentar si el usuario dice que la información no es correcta.
    while True:
        # Pide datos del usuario (nómina, nombre, cantidad).
        nomina, nombre, cantidad = pedir_datos_usuario()

        # Muestra el mensaje de confirmación solicitado.
        respuesta = input(
            f"Bienvenido {nombre}, tu número de nómina es {nomina} y estás intentando subir {cantidad} videos. "
            f"¿Es correcta la información? Sí/No: "
        ).strip()

        # Normaliza la respuesta para comparar sin depender de mayúsculas/minúsculas.
        respuesta_normalizada = respuesta.lower()

        # Si el usuario responde "sí" (aceptamos si/sí/sí).
        if respuesta_normalizada in ("si", "sí", "s"):
            # Captura la información de cada video según cantidad.
            videos = capturar_videos(cantidad)
            # Guarda la salida en salida.txt con el formato requerido.
            guardar_salida(nomina, nombre, cantidad, videos)
            # Muestra confirmación al usuario.
            print("\n✅ Información guardada correctamente en salida.txt")
            # Sale del programa (ya terminó el flujo).
            return

        # Si el usuario responde "no".
        if respuesta_normalizada in ("no", "n"):
            # Pregunta si desea salir del sistema.
            salir = input("¿Deseas salir del sistema? Sí/No: ").strip().lower()
            # Si desea salir, muestra el mensaje final y termina.
            if salir in ("si", "sí", "s"):
                print("Muchas gracias por haber usado nuestro sistema, hasta pronto.")
                return
            # Si no desea salir, el bucle continúa y se vuelven a pedir datos.
            if salir in ("no", "n"):
                print("\n🔁 Perfecto, capturemos nuevamente tus datos.\n")
                continue
            # Si respondió algo diferente, se considera como no válido y se vuelve a iniciar.
            print("\nEntrada no válida. Regresando al inicio.\n")
            continue

        # Si respondió algo diferente a Sí/No, avisamos y reiniciamos.
        print("\nEntrada no válida. Debes contestar Sí o No.\n")


# Punto de entrada estándar en Python para ejecutar el programa.
if __name__ == "__main__":
    # Ejecuta el main dentro del manejador de excepciones.
    ejecutar_con_excepciones(main)
