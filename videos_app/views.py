from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.db import transaction

from .forms import UsuarioCantidadForm, VideoFormSet
from .models import TBL_Usuario, TBL_Video, TBL_UsuarioVideo


@require_http_methods(["GET", "POST"])
def paso1_usuario(request):
    """
    Pantalla 1:
      - nomina, nombre, cantidad
      - botón Aceptar abre modal confirmación (Sí/No)
      - si Sí -> guardamos en session y vamos al paso 2
    """
    if request.method == "POST":
        form = UsuarioCantidadForm(request.POST)
        # confirm viene del modal: "si" o "no"
        confirm = (request.POST.get("confirm") or "").lower()

        if form.is_valid() and confirm == "si":
            data = form.cleaned_data
            request.session["u_nomina"] = data["nomina"]
            request.session["u_nombre"] = data["nombre"]
            request.session["u_cantidad"] = int(data["cantidad"])
            return redirect("paso2_videos")

        # Si presionó "no", solo se queda en la misma pantalla (o limpia)
        # Si no hay confirm o form inválido, renderiza con errores
        return render(request, "videos_app/paso1_usuario.html", {"form": form})

    form = UsuarioCantidadForm()
    return render(request, "videos_app/paso1_usuario.html", {"form": form})


@require_http_methods(["GET", "POST"])
def paso2_videos(request):
    """
    Pantalla 2:
      - Captura de N videos usando Formset (internamente se itera con FOR)
      - Botón Guardar -> BD (PostgreSQL) con transacción
    """
    nomina = request.session.get("u_nomina")
    nombre = request.session.get("u_nombre")
    cantidad = request.session.get("u_cantidad")

    if not (nomina and nombre and cantidad):
        return redirect("paso1_usuario")

    if request.method == "POST":
        formset = VideoFormSet(request.POST)
        if formset.is_valid():
            with transaction.atomic():
                usuario, creado = TBL_Usuario.objects.get_or_create(
                    nomina=nomina,
                    defaults={"nombre": nombre}
                )
                if not creado and usuario.nombre != nombre:
                    usuario.nombre = nombre
                    usuario.save()

                # ✅ CICLO FOR para los N videos (cumple nota)
                for f in formset.cleaned_data:
                    # titulo se captura por requisito pero tu modelo puede no tenerlo
                    video = TBL_Video.objects.create(
                        nombre_video=f["nombre_video"],  # ya viene sin espacios
                        extension=f["extension"],
                        tamano=f["tamano"],
                    )
                    TBL_UsuarioVideo.objects.create(usuario=usuario, video=video)

            # Limpia sesión y muestra éxito
            request.session.pop("u_nomina", None)
            request.session.pop("u_nombre", None)
            request.session.pop("u_cantidad", None)

            return render(request, "videos_app/exito.html")

        return render(request, "videos_app/paso2_videos.html", {
            "formset": formset,
            "cantidad": cantidad,
            "nombre": nombre,
            "nomina": nomina,
        })

    # GET: construye formset con exactamente N forms
    formset = VideoFormSet(initial=[{} for _ in range(int(cantidad))])
    return render(request, "videos_app/paso2_videos.html", {
        "formset": formset,
        "cantidad": cantidad,
        "nombre": nombre,
        "nomina": nomina,
    })

