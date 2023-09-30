from django.urls import path
from . import views

from .views import RegisterView, user_exit,ShopLoginView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"), 
    path("logout/", user_exit, name="logout"),  
    path("login/", ShopLoginView.as_view(), name="login"),
]
 