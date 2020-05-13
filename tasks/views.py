from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

def taskList(requests):
    tasks = Task.objects.all().order_by('-create_at')
    return render(requests, 'task/list.html', {'tasks': tasks})

def taskView(requests, id):
    task = get_object_or_404(Task, pk=id)
    data = {
        'task': task
    }
    return render(requests, 'task/task.html', data)

def newTask(requests):
    if requests.method == 'POST':
        form = TaskForm(requests.POST)

        if form.is_valid():
            task = form.save(commit= False)
            task.done = 'doing'
            task.save()
            return redirect('/')
    else:
        form = TaskForm()
        data = {
            'form': form
        }
        return render(requests, 'task/addtask.html', data)

def helloworld(requests):
    return HttpResponse('Hello World')

def yourname(requests, name):
    return render(requests, 'task/yourname.html', {'name': name})