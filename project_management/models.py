from django.db import models
from django.contrib.auth.models import User

# class Project(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200)
#     title = models.CharField(max_length=200)
#     code = models.CharField(max_length=10000, unique=True)
#     description = models.TextField()