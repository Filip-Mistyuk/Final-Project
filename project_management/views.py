from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import ProjectForm

# def create_project(request):
#     if request.method == 'POST':
#         form = ProjectForm(request.POST)
#         if form.is_valid():
#             # Сохранение данных проекта в базу данных
#             form.save()
#             # После успешного создания проекта, вы можете перенаправить пользователя на другую страницу
#             # Например, на главную страницу
#             return redirect('home')
#     else:
#         form = ProjectForm()
    
#     return render(request, 'home/create_project.html', {'form': form})
