from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Project
from .forms import ProjectForm

class HomePageView(TemplateView):
    template_name = 'home/index.html'

@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            
            project.user = request.user 
            
            project.save()
            
            # После успешного создания проекта перенаправьте пользователя на другую страницу
            return render(request, 'home/index.html')
    else:
        form = ProjectForm()
    
    return render(request, 'home/create_project.html', {'form': form})

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'create_project.html'
    success_url = reverse_lazy('home')