from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import forms
from . import models
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.


# add album class
@method_decorator(login_required, name="dispatch")
class AddAlbumView(CreateView):
    template_name = "add_album.html"
    form_class = forms.AlbumForm
    success_url = reverse_lazy("homepage")

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


# edit album class
@method_decorator(login_required, name="dispatch")
class EditAlbumView(UpdateView):
    model = models.Album
    template_name = "add_album.html"
    pk_url_kwarg = "id"
    form_class = forms.AlbumForm
    success_url = reverse_lazy("homepage")

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


# delete album class
@method_decorator(login_required, name="dispatch")
class DeleteAlbumView(DeleteView):
    model = models.Album
    pk_url_kwarg = "id"
    success_url = reverse_lazy("homepage")
    template_name = "delete_album.html"
