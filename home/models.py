from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render

class Project(models.Model):
    PROJECT_TYPES = [
        ('Game','Игра'), ('Sait','Сайт'),('App','Приложение'), ('Another one','Другое...'),
        # Добавьте другие типы проектов, если необходимо
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=100, choices=PROJECT_TYPES, default='DEFAULT_VALUE')
    # code = models.CharField(max_length=10000, unique=True)
    description = models.TextField()
    project_file = models.FileField(upload_to='files/', default="there is no file.py")
    project_file2 = models.FileField(upload_to='files/', default="there is no file.py")
    project_file3 = models.FileField(upload_to='files/', default="there is no file.py")
    project_file4 = models.FileField(upload_to='files/', default="there is no file.py")

    def __str__(self):
        return self.name


# class ProjectFile(models.Model):
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     file = models.FileField(upload_to='project_files/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.file.name