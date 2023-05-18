from django.urls import path, include

from .views import *
from . import views
from django.contrib.auth.views import LogoutView

from store_chirho.views_chirho.offer_views_chirho import *


urlpatterns = [
    path('', views.IndexChirho.as_view(), name='index_chirho'),
    path('aboutme_chirho/', views.AboutMeChirho.as_view(), name='aboutme_chirho'),
    path('create_offer_chirho/', CreateOfferChirho.as_view(), name='create_offer_chirho'),
    path('<str:post_type_chirho>/list_offer_chirho', ListOfferViewChirho.as_view(), name='list_offer_chirho'),
    path('<uuid:offer_id_chirho>/detail_chirho', DetailOfferChirho.as_view(), name='detail_offer_chirho'),
    path('<uuid:offer_id_chirho>/update_chirho', UpdateOfferChirho.as_view(), name='update_offer_chirho'),

    path('login_chirho/', login_request_chirho, name="login_chirho"),
    path('register_chirho/', register_chirho, name="register_chirho"),
    path('logout_chirho/', LogoutView.as_view(), name="logout_chirho"),
    path('profile_update_chirho/', user_update_chirho, name="profile_update_chirho"),


]