from django.shortcuts import render, redirect, get_object_or_404
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
            files = request.FILES.getlist('files')
            for f in files:
                # Сохранение каждого файла в проекте
                Project.objects.create(project=project, file=f)
            return render(request, 'home/index.html')
    else:
        form = ProjectForm()
    return render(request, 'home/create_project.html', {'form': form})

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'create_project.html'
    success_url = reverse_lazy('home')
    
@login_required
def my_projects(request):
    current_user = request.user

    projects = Project.objects.filter(user=current_user)

    return render(request, 'home/my_projects.html', {'projects': projects})   

def about_us(request):
    return render(request, 'home/about_us.html') 

def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'home/project_detail.html', {'project': project})