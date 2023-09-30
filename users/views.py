from django.shortcuts import render, redirect

from django.views.generic import CreateView, View
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse


class RegisterView(CreateView):
    template_name = "users/register.html"
    form_class = UserCreationForm
    
    def form_valid(self, form: UserCreationForm):
        user = form.save()
        login(self.request, user)
        return redirect("/")


class ShopLoginView(LoginView):
    template_name = "users/login.html"
    form_class = AuthenticationForm


def user_exit(request):
    logout(request)
    return redirect("/")