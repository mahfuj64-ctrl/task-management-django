from django.shortcuts import render, redirect
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm,TaskDetailModelForm
from tasks.models import Employee, Task, TaskDetail, Project
from datetime import date
from django.db.models import Q, Count, Max, Avg, Min
from django.contrib import messages

# Create your views he

def manager_dashboard(request):
    
    
    # total_task = tasks.count()
    # completed_task = Task.objects.filter(status="COMPLETED").count()
    # in_progress_task = Task.objects.filter(status="IN_PROGRESS").count()
    # pending_task = Task.objects.filter(status="PENDING").count()

    # context = {
    #     "tasks": tasks,
    #     "total_task": total_task,
    #     "pending_task": pending_task,
    #     "in_progress_task": in_progress_task,
    #     "completed_task": completed_task
    # }

    type = request.GET.get('type','all')

    counts = Task.objects.aggregate(
        total = Count('id'),
        completed = Count('id',filter=Q(status='COMPLETED')),
        in_progress = Count('id',filter=Q(status='IN_PROGRESS')),
        pending = Count('id',filter=Q(status='PENDING')),
    )

    #Retriving task date

    base_query = Task.objects.select_related("details").prefetch_related("assigned_to")

    if type == 'completed':
            tasks = base_query.filter(status="COMPLETED")
    elif type == 'in_progress':
            tasks = base_query.filter(status="IN_PROGRESS")
    elif type == 'pending':
            tasks = base_query.filter(status="PENDING")
    elif type == 'all':
            tasks = base_query.all()

    context ={
        "tasks": tasks,
        "counts": counts

    }

    return render(request, "dashboard/manager_dashboard.html",context)

def user_dashboard(request):
    return render(request, 'dashboard/user_dashboard.html')
def test(request):
    context = {
        'names': ['Mahfuj','Karim','Habib','John'],
        'age': 27
    }
    return render(request, 'test.html',context)

def create_task(request):
    # employees = Employee.objects.all()

    task_form = TaskModelForm()
    task_detail_form = TaskDetailModelForm()

    if request.method == "POST":
        task_form = TaskModelForm(request.POST)
        task_detail_form = TaskDetailModelForm(request.POST)
        if task_form.is_valid() and task_detail_form:
            """For Model Form Data"""
            # print(form)
            task=task_form.save()
            task_detail=task_detail_form.save(commit=False)
            task_detail.task=task
            task_detail.save()

            messages.success(request,"Task Created Successfully")

            return redirect("create_task")
            """For Django Form Data"""

    context = {"task_form": task_form,"task_detail_form":task_detail_form}
    return render(request, "task_form.html",context)


def view_task(request):

    # tasks = TaskDetail.objects.select_related("task").all()
    tasks = Task.objects.select_related("project").all()
    # tasks = Project.objects.all()

    # tasks = Task.objects.prefetch_related("assigned_to").all()
    # task_count = Task.objects.aggregate(num_task=Count('id'))
    # projects = Project.objects.annotate(num_task=Count('task')).order_by("num_task")
    return render(request,"dashboard/show_task.html",{"tasks": tasks})



def update_task(request,id):
    task = Task.objects.get(id=id)
    task_form = TaskModelForm(instance=task)

    if task.details:
        task_detail_form = TaskDetailModelForm(instance=task.details)

    if request.method == "POST":
        task_form = TaskModelForm(request.POST,instance=task)
        task_detail_form = TaskDetailModelForm(request.POST,instance=task.details)
        if task_form.is_valid() and task_detail_form:
            """For Model Form Data"""
            # print(form)
            task=task_form.save()
            task_detail=task_detail_form.save(commit=False)
            task_detail.task=task
            task_detail.save()

            messages.success(request,"Task Updated Successfully")

            return redirect("update_task",id)
            """For Django Form Data"""

    context = {"task_form": task_form,"task_detail_form":task_detail_form}
    return render(request, "task_form.html",context)

def delete_task(request,id):
     if request.method == 'POST':
          task = Task.objects.get(id=id)
          task.delete()

          messages.success(request, "Task Delete Successfully")
          return redirect('manager_dashboard')
     else:
          messages.success(request, "Something went worng")
          return redirect('manager_dashboard')