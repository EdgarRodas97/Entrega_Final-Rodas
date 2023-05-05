from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from store_chirho.models import PostChirho


class NotebookListOfferViewChirho(LoginRequiredMixin, ListView):
    template_name = "notebook_chirho/notebook_list_offer_chirho.html"
    model = PostChirho
    
    def get_context_data(self, *args, **kwargs):
        context_chirho = super().get_context_data(**kwargs)
        offers_chirho = PostChirho.objects.filter(post_type_chirho = PostChirho.PostTypeChirho.NOTEBOOK_CHIRHO).all()
        #q_chirho = self.request.GET.get("q_chirho", None)
        #context_chirho['q_chirho'] = q_chirho
        context_chirho['offers_chirho'] = offers_chirho
        return context_chirho