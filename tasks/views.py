from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from datetime import datetime , timedelta
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import UserLoginForm, UserRegistrationForm

def Task_list(request):
    tasks = Task.objects.all()
    return render(request,'tasks/Task_list.html',{'tasks':tasks})


def Task_detail(request,task_id):
    task=Task.objects.get(id=task_id,user=request.user)
    return render(request,'tasks/Task_detail.html',{'task':task})

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

def filter_task(request):
    filter_type=request.GET.get('filter','all')
    today=datetime.today()

    if filter_type == 'weekly':
        start_of_week=today - timedelta(days=today.weekday())
        end_of_week=start_of_week + timedelta (days=6)
        tasks=Task.objects.filter(due_date__range=[start_of_week,end_of_week])

    elif filter_type == 'monthly':
        current_month=today.month
        current_year=today.year
        tasks=Task.objects.filter(due_date_month=[current_month,current_year])
    elif filter_type == 'yearly':
        current_year=today.year
        tasks=Task.objects.filter(due_date_year=current_year)
    elif filter_type == 'complited':
        tasks=Task.objects.filter(complited=True)
    elif filter_type == 'incomplited':
        tasks=Task.objects.filter(complited=False)
    elif filter_type == 'task_day':
        tasks=Task.objects.filter(task_day=True)
    elif filter_type == 'task_week':
        tasks=Task.objects.filter(task_week=True)
    elif filter_type == 'task_month':
        tasks=Task.objects.filter(task_month=True)
    elif filter_type == 'task_year':
        tasks=Task.objects.filter(task_year=True)

    else:
        tasks=Task.objects.all()

    return render(request, 'tasks/Task_list.html',{'tasks':tasks})

def filter_by_date (request):
    start_date=request.GET.get('start_date')
    end_date=request.GET.get('end_date')

    if start_date and end_date :
        tasks=Task.objects.filter(due_date__range=[start_date,end_date])
    else:
        tasks=Task.objects.all()

    return render(request ,'tasks/Task_list.html',{'tasks':tasks})
    
def login_register_view(request):
    if request.method == 'POST':
        if 'login_submit' in request.POST:  # إذا كان المستخدم يقوم بتسجيل الدخول
            login_form = UserLoginForm(request, data=request.POST)
            register_form = UserRegistrationForm()

            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('accounts')  # غير المسار للصفحة التي ترغب في إعادة التوجيه إليها
        elif 'register_submit' in request.POST:  # إذا كان المستخدم يقوم بإنشاء حساب
            login_form = UserLoginForm()
            register_form = UserRegistrationForm(request.POST)

            if register_form.is_valid():
                user = register_form.save(commit=False)
                user.set_password(register_form.cleaned_data['password'])
                user.save()
                return redirect('accounts')  # بعد إنشاء الحساب، يقوم بتوجيهه إلى صفحة تسجيل الدخول

    else:
        login_form = UserLoginForm()
        register_form = UserRegistrationForm()

    return render(request, 'registration/login.html', {'login_form': login_form, 'register_form': register_form})