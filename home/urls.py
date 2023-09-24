from django.urls import path
from .views import HomePageView  
from . import views

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path('create_project/', views.create_project, name='create_project'),
]