from django.urls import path
from .views import HomePageView  
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('create_project/', views.create_project, name='create_project'),
    path('my_projects/', views.my_projects, name='my_projects'),
    path('about_us/', views.about_us, name='about_us'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
]