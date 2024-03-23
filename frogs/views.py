from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from frogs.models import Frog
from frogs.forms import FrogCreateForm, FrogEditForm


@login_required()
def index(request):
    frogs = Frog.objects.filter(status_id__lt=5).order_by('status', 'title')
    context = {
        'frogs': frogs
    }
    return render(request, 'frogs/index.html', context)


@login_required()
def view(request, **kwargs):
    frog_id = kwargs['id']
    frog = Frog.objects.get(pk=frog_id)
    print('frog', frog)
    context = {
        'frog': frog,
    }
    return render(request, 'frogs/view.html', context)


@login_required()
def edit(request, **kwargs):
    if request.method == 'POST':
        frog = Frog.objects.get(pk=kwargs['id'])
        form = FrogEditForm(request.POST, instance=frog)
        if form.is_valid():
            form.save()
            return redirect('/frogs/view/' + str(kwargs['id']))
        return redirect('/frogs')
    frog = Frog.objects.get(pk=kwargs['id'])
    form = FrogEditForm(instance=frog)
    return render(request, 'frogs/edit.html', {'form': form})


@login_required()
def create(request):
    if request.method == 'POST':
        form = FrogCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/frogs')
        return redirect('/frogs/create')
    form = FrogCreateForm()
    return render(request, 'frogs/create.html', {'form': form})


@login_required()
def update(request, **kwargs):
    status = int(request.GET.get('status'))
    if status < 1: status = 1
    if status > 6: status = 6
    frog = Frog.objects.get(pk=kwargs['id'])
    frog.status_id = status
    frog.save()
    return redirect('/frogs')
