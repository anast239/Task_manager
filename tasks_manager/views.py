from django.shortcuts import render

from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required

from .models import Task
from .forms import TaskForm

def index(request):
    """Домашняя страница приложения Task Manager"""
    return render(request, 'tasks_manager/index.html')

@login_required
def tasks(request):
    """Вывод список заданий"""
    tasks = Task.objects.filter(owner=request.user).order_by('due_date', 'time')
    context = {'tasks' : tasks}
    return render(request, 'tasks_manager/tasks.html', context)

@login_required
def new_task(request):
    """Определяет новую тему."""
    if request.method != 'POST':
        #Данные не отправлялись; создается пустая форма.
        form = TaskForm()
    else:
        #Отправлены данные POST; обработать данные.
        form = TaskForm(data=request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.owner = request.user
            new_task.save()
            return HttpResponseRedirect(reverse('tasks_manager:tasks'))

    context = {'form': form}
    return render(request, 'tasks_manager/new_task.html', context)

def edit_task(request, task_id):
    """Редактирует существующие задание"""
    task = Task.objects.get(id=task_id)
    if request.method != 'POST':
        # Исходный запрос; форма заполняется данными текущей записи.
        form = TaskForm(instance=task)
    else:
        #Отправлены данные POST; обработать данные.
        form = TaskForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tasks_manager:tasks'))
    context = {'task': task, 'form': form}
    return render(request, 'tasks_manager/edit_task.html', context)
        

