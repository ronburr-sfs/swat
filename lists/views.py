from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from lists.models import List
from lists.forms import ListCreateForm, ListEditForm
from items.models import Item


@login_required()
def index(request):
    lists = List.objects.all().order_by('status', 'title')
    context = {
        'lists': lists
    }
    return render(request, 'lists/index.html', context)


@login_required()
def view(request, **kwargs):
    list_id = kwargs['id']
    list = List.objects.get(pk=list_id)
    items = Item.objects.filter(list_id=list_id).order_by('title')
    context = {
        'list': list,
        'items': items,
    }
    return render(request, 'lists/view.html', context)


@login_required()
def edit(request, **kwargs):
    if request.method == 'POST':
        list = List.objects.get(pk=kwargs['id'])
        form = ListEditForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            return redirect('/lists/view/' + str(kwargs['id']))
        return redirect('/lists')
    list = List.objects.get(pk=kwargs['id'])
    form = ListEditForm(instance=list)
    return render(request, 'lists/edit.html', {'form': form})


@login_required()
def create(request):
    if request.method == 'POST':
        form = ListCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/lists')
        return redirect('/lists/create')
    form = ListCreateForm()
    return render(request, 'lists/create.html', {'form': form})


@login_required()
def delete(request, **kwargs):
    list = List.objects.get(pk=kwargs['id'])
    list.delete()
    return redirect('/lists')
