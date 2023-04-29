from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView


class NotebookListOfferViewChirho(TemplateView):
    template_name = "notebook_chirho/notebook_list_offer_chirho.html"