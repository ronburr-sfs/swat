from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from projects.models import Project
from projects.forms import ProjectCreateForm, ProjectEditForm

from tasks.models import Task


@login_required()
def index(request):
    projects = Project.objects.all().order_by('priority', 'title')
    print(projects)
    context = {
        "projects": projects,
    }
    return render(request, 'projects/index.html', context)


@login_required()
def view(request, **kwargs):
    project_id = kwargs['id']
    project = Project.objects.get(pk=project_id)
    tasks = Task.objects.filter(project_id=project_id)
    view_context = {
        'project': project,
        'tasks': tasks,
    }
    return render(request, 'projects/view.html', view_context)


@login_required()
def edit(request, **kwargs):
    if request.method == 'POST':
        project = Project.objects.get(pk=kwargs['id'])
        form = ProjectEditForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('/projects/view/' + str(kwargs['id']))
        return redirect('/projects')
    project = Project.objects.get(pk=kwargs['id'])
    form = ProjectEditForm(instance=project)
    return render(request, 'projects/edit.html', {'form': form})


@login_required()
def create(request):
    if request.method == 'POST':
        form = ProjectCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/projects')
        return redirect('/projects/create')
    form = ProjectCreateForm()
    return render(request, 'projects/create.html', {'form': form})


@login_required()
def delete(request, **kwargs):
    obj = Project.objects.get(pk=kwargs['id'])
    obj.delete()
    return redirect('/projects')
