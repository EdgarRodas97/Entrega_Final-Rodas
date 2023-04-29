from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView


class MonitorListOfferViewChirho(TemplateView):
    template_name = "monitor_chirho/monitor_list_offer_chirho.html"