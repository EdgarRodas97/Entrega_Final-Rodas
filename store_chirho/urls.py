from django.urls import path

from .views import *
from . import views
from django.contrib.auth.views import LogoutView

from store_chirho.views_chirho.computer_views_chirho import *
from store_chirho.views_chirho.gaming_views_chirho import *
from store_chirho.views_chirho.monitor_views_chirho import *
from store_chirho.views_chirho.notebook_views_chirho import *
from store_chirho.views_chirho.tv_views_chirho import *
from store_chirho.views_chirho.offer_views_chirho import *


urlpatterns = [
    path('', views.IndexChirho.as_view(), name='index_chirho'),
    path('aboutme_chirho/', views.AboutMeChirho.as_view(), name='aboutme_chirho'),
    path('create_offer_chirho/', CreateOfferChirho.as_view(), name='create_offer_chirho'),
    path('computer_list_offer_chirho/', ComputerListOfferViewChirho.as_view(), name='computer_list_offer_chirho'),
    path('gaming_list_offer_chirho/', GamingListOfferViewChirho.as_view(), name='gaming_list_offer_chirho'),
    path('monitor_list_offer_chirho/', MonitorListOfferViewChirho.as_view(), name='monitor_list_offer_chirho'),
    path('notebook_list_offer_chirho/', NotebookListOfferViewChirho.as_view(), name='notebook_list_offer_chirho'),
    path('tv_list_offer_chirho/', TvListOfferViewChirho.as_view(), name='tv_list_offer_chirho'),

    path('login_chirho/', login_request_chirho, name="login_chirho"),
    path('register_chirho/', register_chirho, name="register_chirho"),
    path('logout_chirho/', LogoutView.as_view(), name="logout_chirho"),
    path('profile_update_chirho/', user_update_chirho, name="profile_update_chirho"),


]