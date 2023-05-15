from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from .forms import RegisterUserFormChirho, UserEditForm, CreateOfferFormChirho
from django.views.generic import TemplateView, CreateView, ListView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import PostChirho
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User


class IndexChirho(LoginRequiredMixin, ListView):
    template_name = "index_chirho.html"
    model = PostChirho
    
    def get_context_data(self, *args, **kwargs):
        context_chirho = super().get_context_data(**kwargs)
        user_chirho = get_object_or_404(User, id=self.request.user.pk)
        offers_chirho = PostChirho.objects.filter(user_chirho=user_chirho).all()
        #q_chirho = self.request.GET.get("q_chirho", None)
        #context_chirho['q_chirho'] = q_chirho
        context_chirho['offers_chirho'] = offers_chirho
        return context_chirho
    
    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset()


class AboutMeChirho(LoginRequiredMixin, TemplateView):
    template_name = "aboutme_chirho.html"


def login_request_chirho(request):
    if request.method=="POST":
        form= AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            user_chirho=info["username"]
            pass_chirho=info["password"]
            user_auth_chirho=authenticate(username=user_chirho, password=pass_chirho)
            if user_auth_chirho is not None:
                login(request, user_auth_chirho)
                return render(request, "index_chirho.html", {"message_chirho":f"Usuario {user_chirho} logeado correctamente"})
            else:
                return render(request, "login_chirho.html", {"form": form, "message_chirho":"Usuario o contraseña incorrectos" })
        else:
            return render(request, "login_chirho.html", {"form": form, "message_chirho":"Usuario o contraseña incorrectos" })    
    else:
        form=AuthenticationForm()
        return render(request, "login_chirho.html", {"form": form})


def register_chirho(request):
    if request.method=="POST":
        form= RegisterUserFormChirho(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            return render(request, "login_chirho.html", {"message_chirho":f"Usuario creado exitosamente"}) 
        else:
            return render(request, "register_chirho.html", {"form": form, "message_chirho":"Error al crear usuario" })
    else:
        form= RegisterUserFormChirho()
        return render(request, "register_chirho.html", {"form": form})


@login_required
def user_update_chirho(request):
    user_chirho=request.user

    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            user_chirho.email=info["email_chirho"]
            user_chirho.password1=info["password1"]
            user_chirho.password2=info["password2"]
            user_chirho.first_name=info["first_name"]
            user_chirho.last_name=info["last_name"]
            user_chirho.save()
            return render(request, "index_chirho.html", {"message_chirho":f"Usuario modificado correctamente"})
        else:
            return render(request, "user_update_chirho.html", {"form": form, "userchirho":user_chirho.username})
    else:
        form=UserEditForm(instance=user_chirho)
        return render(request, "user_update_chirho.html", {"form": form, "userchirho":user_chirho.username})





    
    


