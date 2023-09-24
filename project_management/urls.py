from django.urls import path
from . import views

urlpatterns = [
    # Другие URL маршруты вашего приложения
    path('create_project/', views.create_project, name='create_project'),
]