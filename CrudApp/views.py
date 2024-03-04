from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from .form import TaskForm

# Create your views here.
def task_list(request):
    tasks= Task.objects.all()
    return render(request,  'task_list.html',{'task': tasks})

def task_detail(request):
    task = get_object_or_404(Task,id=id)
    return render(request, template_name='task_details.html', context={'task':task})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request,template_name='task_form.html',context={'form':form})

def task_edit(request,id):
    task = get_object_or_404(Task,id=id)
    if request.method == 'POST':
        form = TaskForm(request,POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail')
    else:
        form = TaskForm(instance=task)
    return render(request,template_name='task_form.html',context={'form':form})

def task_delete(request,id):
    task = get_object_or_404(Task,id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    else:
        task = TaskForm(instance=task)
    return render(request, template_name='task_confirm_delete.html', context={'task':task})


