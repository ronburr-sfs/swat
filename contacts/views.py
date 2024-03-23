from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from contacts.models import Contact
from contacts.forms import ContactCreateForm, ContactEditForm


@login_required()
def index(request):
    contacts = Contact.objects.all().order_by('-id')[:5]
    context = {
        'contacts': contacts
    }
    return render(request, 'contacts/index.html', context)


@login_required()
def view(request, **kwargs):
    contact_id = kwargs['id']
    contact = Contact.objects.get(pk=contact_id)
    context = {
        'contact': contact
    }
    return render(request, 'contacts/view.html', context)


@login_required()
def edit(request, **kwargs):
    if request.method == 'POST':
        contact = Contact.objects.get(pk=kwargs['id'])
        form = ContactEditForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('/contacts/view/' + str(kwargs['id']))
        return redirect('/contacts')
    contact = Contact.objects.get(pk=kwargs['id'])
    form = ContactEditForm(instance=contact)
    return render(request, 'contacts/edit.html', {'form': form})


@login_required()
def create(request):
    if request.method == 'POST':
        form = ContactCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contacts')
        return redirect('/contacts/create')
    form = ContactCreateForm()
    return render(request, 'contacts/create.html', {'form': form})


@login_required()
def delete(request, **kwargs):
    contact = Contact.objects.get(pk=kwargs['id'])
    contact.delete()
    return redirect('/contacts')
