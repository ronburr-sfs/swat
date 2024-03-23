from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from cloneapps.models import Cloneapp
from cloneapps.forms import CloneappCreateForm, CloneappEditForm


@login_required()
def index(request):
    cloneapps = Cloneapp.objects.all().order_by('-id')[:5]
    context = {
        'cloneapps': cloneapps
    }
    return render(request, 'cloneapps/index.html', context)


@login_required()
def view(request, **kwargs):
    cloneapp_id = kwargs['id']
    cloneapp = Cloneapp.objects.get(pk=cloneapp_id)
    context = {
        'cloneapp': cloneapp
    }
    return render(request, 'cloneapps/view.html', context)


@login_required()
def edit(request, **kwargs):
    if request.method == 'POST':
        cloneapp = Cloneapp.objects.get(pk=kwargs['id'])
        form = CloneappEditForm(request.POST, instance=cloneapp)
        if form.is_valid():
            form.save()
            return redirect('/cloneapps/view/' + str(kwargs['id']))
        return redirect('/cloneapps')
    cloneapp = Cloneapp.objects.get(pk=kwargs['id'])
    form = CloneappEditForm(instance=cloneapp)
    return render(request, 'cloneapps/edit.html', {'form': form})


@login_required()
def create(request):
    if request.method == 'POST':
        form = CloneappCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/cloneapps')
        return redirect('/cloneapps/create')
    form = CloneappCreateForm()
    return render(request, 'cloneapps/create.html', {'form': form})


@login_required()
def delete(request, **kwargs):
    cloneapp = Cloneapp.objects.get(pk=kwargs['id'])
    cloneapp.delete()
    return redirect('/cloneapps')
