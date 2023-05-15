
from typing import Any, Optional
from django.db import models
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from store_chirho.forms import CreateOfferFormChirho
from django.contrib import messages
from django.urls import reverse
from store_chirho.models import PostChirho
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib.auth.models import User


class ListOfferViewChirho(LoginRequiredMixin, ListView):
    template_name = "offer_chirho/list_offer_chirho.html"
    model = PostChirho
    
    def get_context_data(self, *args, **kwargs):
        context_chirho = super().get_context_data(**kwargs)
        post_type_chirho = self.kwargs['post_type_chirho']
        offers_chirho = PostChirho.objects.filter(post_type_chirho=post_type_chirho).all()
        #q_chirho = self.request.GET.get("q_chirho", None)
        #context_chirho['q_chirho'] = q_chirho
        context_chirho['offers_chirho'] = offers_chirho
        context_chirho['post_type_chirho'] = post_type_chirho
        context_chirho['post_type_label_chirho'] = dict(PostChirho.PostTypeChirho.choices)[post_type_chirho]
        return context_chirho


class CreateOfferChirho(LoginRequiredMixin, CreateView):
    template_name = "offer_chirho/create_offer_chirho.html"
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
    

class DetailOfferChirho(LoginRequiredMixin, DetailView):
    template_name = "offer_chirho/offer_detail_chirho.html"
    model = PostChirho
     
    def get_context_data(self, *args, **kwargs):
        context_chirho = super().get_context_data(**kwargs)
        context_chirho["offers_chirho"] = get_object_or_404(PostChirho, id_chirho=self.kwargs['offer_id_chirho'])
        return context_chirho
    
    def get_object(self):
        return PostChirho.objects.get(pk=self.kwargs['offer_id_chirho'])
    
