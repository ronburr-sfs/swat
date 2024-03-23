from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from comments.models import Comment
from comments.forms import CommentCreateForm, CommentEditForm


@login_required()
def index(request):
    comments = Comment.objects.all().order_by('-id')[:5]
    context = {
        'comments': comments
    }
    return render(request, 'comments/index.html', context)


@login_required()
def view(request, **kwargs):
    comment_id = kwargs['id']
    comment = Comment.objects.get(pk=comment_id)
    context = {
        'comment': comment
    } 
    return render(request, 'comments/view.html', context)


@login_required()
def edit(request, **kwargs):
    if request.method == 'POST':
        comment = Comment.objects.get(pk=kwargs['id'])
        form = CommentEditForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('/comments/view/' + str(kwargs['id']))
        return redirect('/comments')
    comment = Comment.objects.get(pk=kwargs['id'])
    form = CommentEditForm(instance=comment)
    return render(request, 'comments/edit.html', {'form': form})


@login_required()
def create(request):
    if request.method == 'POST':
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('/comments')
        return redirect('/comments/create')
    form = CommentCreateForm()
    return render(request, 'comments/create.html', {'form': form})


@login_required()
def delete(request, **kwargs):
    comment = Comment.objects.get(pk=kwargs['id'])
    comment.delete()
    return redirect('/comments')
