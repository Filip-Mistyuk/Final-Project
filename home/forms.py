from django import forms
from .models import Project
        
class ProjectForm(forms.ModelForm):
    # files = forms.FileField(widget=forms.ClearableMultipleFilesInput(attrs={'multiple': True}), required=False)
    
    class Meta:
        model = Project
        fields = ['name', 'type','description', 'project_file', 'project_file2', 'project_file3', 'project_file4']
        
# class ProjectFileForm(forms.ModelForm):
#     class Meta:
#         model = ProjectFile
#         fields = ['file']