from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from tasks.models import Task
from tasks.forms import TaskCreateForm, TaskEditForm


@login_required()
def index(request):
    tasks = Task.objects.filter(status_id__lt=6).order_by('project', 'title')
    context = {
        'tasks': tasks
    }
    return render(request, 'tasks/index.html', context)


@login_required()
def view(request, **kwargs):
    task_id = kwargs['id']
    task = Task.objects.get(pk=task_id)
    context = {
        'task': task
    }
    return render(request, 'tasks/view.html', context)


@login_required()
def edit(request, **kwargs):
    if request.method == 'POST':
        task = Task.objects.get(pk=kwargs['id'])
        form = TaskEditForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/tasks/view/' + str(kwargs['id']))
        return redirect('/tasks')
    task = Task.objects.get(pk=kwargs['id'])
    form = TaskEditForm(instance=task)
    return render(request, 'tasks/edit.html', {'form': form})


@login_required()
def create(request):
    if request.method == 'POST':
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/tasks')
        return redirect('/tasks/create')
    form = TaskCreateForm()
    return render(request, 'tasks/create.html', {'form': form})


@login_required()
def delete(request, **kwargs):
    task = Task.objects.get(pk=kwargs['id'])
    task.delete()
    return redirect('/tasks')
