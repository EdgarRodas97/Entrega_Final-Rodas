from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView


class ComputerListOfferViewChirho(TemplateView):
    template_name = "computer_chirho/computer_list_offer_chirho.html"