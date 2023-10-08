from django import forms
from .models import Project
        
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'title','description', 'project_file']
        
# class ProjectFileForm(forms.ModelForm):
#     class Meta:
#         model = ProjectFile
#         fields = ['file']