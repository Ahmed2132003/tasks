from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm

def Task_list(request):
    tasks = Task.objects.all()
    return render(request,'tasks/Task_list.html',{'tasks':tasks})


def Task_detail(request,task_id):
    task=Task.objects.get(id=task_id,user=request.user)
    return render(request,'task/Task_detail.html',{'task':task})

def Task_create(request):
    if request.method == 'POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            task=form.save(commit=False)
            task.user=request.user
            task.save()
            return redirect('Task_list')
    else:
        form=TaskForm()
    return render(request,'tasks/Task_form.html',{'form':form})
def Task_update(request,task_id):
    task=Task.objects.get(id=task_id,user=request.user)
    if request.method == 'POST':
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('Task_list')
    else:
        form=TaskForm(instance=task)
    return render(request,'tasks/Task_form.html',{'form':form})
def Task_delete(request,task_id):
    task=Task.objects.get(id=task_id,user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('Task_list')
    return render(request,'tasks/Task_confirm_delete.html',{'task':task})

