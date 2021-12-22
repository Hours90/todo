from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator

from .forms import *
from .models import *
# Create your views here.

@login_required
def index(request):
    tasks = Task.objects.filter(owner = request.user).order_by('-created')

    paginator = Paginator(tasks, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(data = request.POST)
        if form.is_valid():
            new_task = form.save(commit = False)
            new_task.owner = request.user
            new_task.save()
            return redirect('/')

    return render(request, 'tasks/index.html', {'form':form, 'page_obj': page_obj})

@login_required
def edit_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance = task)

    if request.method == 'POST':
        form = TaskForm(request.POST,instance = task)
        if form.is_valid():
            edit_task = form.save(commit = False)
            edit_task.owner = request.user
            edit_task.save()
            return redirect('/')
    
    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task })

@login_required
def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'tasks/delete.html', {'task': task })
