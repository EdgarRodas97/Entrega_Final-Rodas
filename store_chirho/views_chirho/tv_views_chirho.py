from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView


class TvListOfferViewChirho(TemplateView):
    template_name = "tv_chirho/tv_list_offer_chirho.html"