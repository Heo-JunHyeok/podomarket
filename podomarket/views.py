from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
from allauth.account.views import PasswordChangeView
from .models import Post


# Create your views here.
class IndexView(ListView):
    model = Post
    template_name = "podomarket/index.html"
    paginate_by = 8
    ordering = ["-dt_created"]


class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse("index")
