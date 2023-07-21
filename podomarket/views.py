from django.shortcuts import render
from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from allauth.account.views import PasswordChangeView
from .models import Post


# Create your views here.
class IndexView(ListView):
    model = Post
    template_name = "podomarket/index.html"
    paginate_by = 8
    ordering = ["-dt_created"]


class PostDetailView(DetailView):
    model = Post
    template_name = "podomarket/post_detail.html"
    pk_url_kwarg = "post_id"


class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse("index")
