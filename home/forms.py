from django import forms
from .models import Project, ProjectFile
        
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'title', 'code', 'description', 'project_file']
        
class ProjectFileForm(forms.ModelForm):
    class Meta:
        model = ProjectFile
        fields = ['file']