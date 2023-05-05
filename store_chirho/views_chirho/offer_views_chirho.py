
from django.views.generic import TemplateView, CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from store_chirho.forms import CreateOfferFormChirho
from django.contrib import messages
from django.urls import reverse
from store_chirho.models import PostChirho
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib.auth.models import User


class CreateOfferChirho(LoginRequiredMixin, CreateView):
    template_name ="offer_chirho/create_offer_chirho.html"
    form_class = CreateOfferFormChirho

    def form_valid(self, form):
        form.instance.user_chirho = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs_chirho = super().get_form_kwargs()
        return kwargs_chirho

    def get_success_url(self):
        messages.success(self.request, "Exito en crear publicación")
        return reverse('index_chirho')
