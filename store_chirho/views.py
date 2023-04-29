from django.shortcuts import render
from django.views.generic import TemplateView



class CreateOfferChirho(TemplateView):
    template_name ="create_offer_chirho.html"


class IndexChirho(TemplateView):
    template_name = "index_chirho.html"


class AboutMeChirho(TemplateView):
    template_name = "aboutme_chirho.html"





    
    


