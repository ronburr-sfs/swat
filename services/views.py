from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from services.models import Service
from services.forms import ServiceCreateForm, ServiceEditForm


@login_required()
def index(request):
    services = Service.objects.all().order_by('-id')[:5]
    context = {
        'services': services
    }
    return render(request, 'services/index.html', context)


@login_required()
def view(request, **kwargs):
    service_id = kwargs['id']
    service = Service.objects.get(pk=service_id)
    context = {
        'service': service
    }
    return render(request, 'services/view.html', context)


@login_required()
def edit(request, **kwargs):
    if request.method == 'POST':
        service = Service.objects.get(pk=kwargs['id'])
        form = ServiceEditForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('/services/view/' + str(kwargs['id']))
        return redirect('/services')
    service = Service.objects.get(pk=kwargs['id'])
    form = ServiceEditForm(instance=service)
    return render(request, 'services/edit.html', {'form': form})


@login_required()
def create(request):
    if request.method == 'POST':
        form = ServiceCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/services')
        return redirect('/services/create')
    form = ServiceCreateForm()
    return render(request, 'services/create.html', {'form': form})


@login_required()
def delete(request, **kwargs):
    service = Service.objects.get(pk=kwargs['id'])
    service.delete()
    return redirect('/services')
