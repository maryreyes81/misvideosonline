from django.urls import path
from . import views
from . import views_crud
from . import views_crud_users

urlpatterns = [
    # Flujo de tu proyecto (Paso 1 y Paso 2)
    path("", views.paso1_usuario, name="paso1_usuario"),
    path("videos/", views.paso2_videos, name="paso2_videos"),

    # CRUD de videos
    path("crud/videos/", views_crud.VideoListView.as_view(), name="video_list"),
    path("crud/videos/nuevo/", views_crud.VideoCreateView.as_view(), name="video_create"),
    path("crud/videos/<int:pk>/editar/", views_crud.VideoUpdateView.as_view(), name="video_update"),
    path("crud/videos/<int:pk>/borrar/", views_crud.VideoDeleteView.as_view(), name="video_delete"),

 # ✅ CRUD de usuarios
    path("crud/usuarios/", views_crud_users.UsuarioListView.as_view(), name="usuario_list"),
    path("crud/usuarios/nuevo/", views_crud_users.UsuarioCreateView.as_view(), name="usuario_create"),
    path("crud/usuarios/<int:pk>/editar/", views_crud_users.UsuarioUpdateView.as_view(), name="usuario_update"),
    path("crud/usuarios/<int:pk>/borrar/", views_crud_users.UsuarioDeleteView.as_view(), name="usuario_delete"),

    # ✅ CRUD de relación usuario-video (muestra nómina + video y demás)
    path("crud/usuario-videos/", views_crud_users.UsuarioVideoListView.as_view(), name="usuariovideo_list"),
    path("crud/usuario-videos/nuevo/", views_crud_users.UsuarioVideoCreateView.as_view(), name="usuariovideo_create"),
    path("crud/usuario-videos/<int:pk>/editar/", views_crud_users.UsuarioVideoUpdateView.as_view(), name="usuariovideo_update"),
    path("crud/usuario-videos/<int:pk>/borrar/", views_crud_users.UsuarioVideoDeleteView.as_view(), name="usuariovideo_delete"),
]