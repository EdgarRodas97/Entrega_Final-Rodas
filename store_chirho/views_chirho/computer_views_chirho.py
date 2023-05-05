from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from store_chirho.models import PostChirho
from django.contrib.auth.models import User

class ComputerListOfferViewChirho(LoginRequiredMixin, ListView):
    template_name = "computer_chirho/computer_list_offer_chirho.html"
    model = PostChirho
    
    def get_context_data(self, *args, **kwargs):
        context_chirho = super().get_context_data(**kwargs)
        offers_chirho = PostChirho.objects.filter(post_type_chirho = PostChirho.PostTypeChirho.COMPUTER_CHIRHO).all()
        #q_chirho = self.request.GET.get("q_chirho", None)
        #context_chirho['q_chirho'] = q_chirho
        context_chirho['offers_chirho'] = offers_chirho
        return context_chirho