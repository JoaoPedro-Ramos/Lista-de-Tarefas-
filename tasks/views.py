from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from django.contrib import messages




@login_required
def taskList(requests):
    tasks_list = Task.objects.all().order_by('-create_at')

    paginator = Paginator(tasks_list, 3)

    page = requests.GET.get('page')

    tasks = paginator.get_page(page)
    return render(requests, 'task/list.html', {'tasks': tasks})

@login_required
def taskView(requests, id):
    task = get_object_or_404(Task, pk=id)
    data = {
        'task': task
    }
    return render(requests, 'task/task.html', data)

@login_required
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

@login_required
def editTask(requests, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)
    data = {
        'form': form,
        'task': task
    }
    if requests.method == 'POST': 
        form = TaskForm(requests.POST, instance=task)

        if form.is_valid():
            task.save()
            print('válido')
            return redirect('/')
        else:
            print('inválido')
            return render(requests, 'task/edittask.html', data)
    else:
        print('Não é o método POST')
        return render(requests, 'task/edittask.html', data)

@login_required
def deleteTask(requests, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()

    messages.info(requests, 'Tarefa deletada com sucesso!')

    return redirect('/')
    

def helloworld(requests):
    return HttpResponse('Hello World')

def yourname(requests, name):
    return render(requests, 'task/yourname.html', {'name': name})