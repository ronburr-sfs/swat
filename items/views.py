from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from items.models import Item
from items.forms import ItemCreateForm, ItemEditForm


@login_required()
def index(request):
    items = Item.objects.all().order_by('list', 'title')
    context = {
        'items': items
    }
    return render(request, 'items/index.html', context)


@login_required()
def view(request, **kwargs):
    item_id = kwargs['id']
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item
    }
    return render(request, 'items/view.html', context)


@login_required()
def edit(request, **kwargs):
    if request.method == 'POST':
        item = Item.objects.get(pk=kwargs['id'])
        form = ItemEditForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/items/view/' + str(kwargs['id']))
        return redirect('/items')
    item = Item.objects.get(pk=kwargs['id'])
    form = ItemEditForm(instance=item)
    return render(request, 'items/edit.html', {'form': form})


@login_required()
def create(request):
    if request.method == 'POST':
        form = ItemCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/items')
        return redirect('/items/create')
    form = ItemCreateForm()
    return render(request, 'items/create.html', {'form': form})


@login_required()
def delete(request, **kwargs):
    item = Item.objects.get(pk=kwargs['id'])
    item.delete()
    return redirect('/items')
