from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import TBL_Video
from .forms_crud import VideoModelForm

class VideoListView(ListView):
    model = TBL_Video
    template_name = "videos_app/crud/video_list.html"
    context_object_name = "videos"
    ordering = ["-id"]

class VideoCreateView(CreateView):
    model = TBL_Video
    form_class = VideoModelForm
    template_name = "videos_app/crud/video_form.html"
    success_url = reverse_lazy("video_list")

class VideoUpdateView(UpdateView):
    model = TBL_Video
    form_class = VideoModelForm
    template_name = "videos_app/crud/video_form.html"
    success_url = reverse_lazy("video_list")

class VideoDeleteView(DeleteView):
    model = TBL_Video
    template_name = "videos_app/crud/video_confirm_delete.html"
    success_url = reverse_lazy("video_list")
