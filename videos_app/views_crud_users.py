from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Count

from .models import TBL_Usuario, TBL_UsuarioVideo
from .forms_crud_users import UsuarioModelForm, UsuarioVideoModelForm


# -------- CRUD USUARIOS --------

class UsuarioListView(ListView):
    model = TBL_Usuario
    template_name = "videos_app/crud/usuario_list.html"
    context_object_name = "usuarios"
    ordering = ["-id"]

    def get_queryset(self):
        # cuenta cuántos videos tiene cada usuario (por relación)
        return TBL_Usuario.objects.annotate(total_videos=Count("tbl_usuariovideo")).order_by("-id")


class UsuarioCreateView(CreateView):
    model = TBL_Usuario
    form_class = UsuarioModelForm
    template_name = "videos_app/crud/usuario_form.html"
    success_url = reverse_lazy("usuario_list")


class UsuarioUpdateView(UpdateView):
    model = TBL_Usuario
    form_class = UsuarioModelForm
    template_name = "videos_app/crud/usuario_form.html"
    success_url = reverse_lazy("usuario_list")


class UsuarioDeleteView(DeleteView):
    model = TBL_Usuario
    template_name = "videos_app/crud/usuario_confirm_delete.html"
    success_url = reverse_lazy("usuario_list")


# -------- CRUD RELACIÓN USUARIO-VIDEO --------

class UsuarioVideoListView(ListView):
    model = TBL_UsuarioVideo
    template_name = "videos_app/crud/usuariovideo_list.html"
    context_object_name = "relaciones"
    ordering = ["-id"]

    def get_queryset(self):
        # trae usuario y video de una vez (más rápido)
        return TBL_UsuarioVideo.objects.select_related("usuario", "video").order_by("-id")


class UsuarioVideoCreateView(CreateView):
    model = TBL_UsuarioVideo
    form_class = UsuarioVideoModelForm
    template_name = "videos_app/crud/usuariovideo_form.html"
    success_url = reverse_lazy("usuariovideo_list")


class UsuarioVideoUpdateView(UpdateView):
    model = TBL_UsuarioVideo
    form_class = UsuarioVideoModelForm
    template_name = "videos_app/crud/usuariovideo_form.html"
    success_url = reverse_lazy("usuariovideo_list")


class UsuarioVideoDeleteView(DeleteView):
    model = TBL_UsuarioVideo
    template_name = "videos_app/crud/usuariovideo_confirm_delete.html"
    success_url = reverse_lazy("usuariovideo_list")
