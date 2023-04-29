from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView


class GamingListOfferViewChirho(TemplateView):
    template_name = "gaming_chirho/gaming_list_offer_chirho.html"