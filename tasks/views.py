from django.shortcuts import render
from .models import Task

# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    to_do_tasks = tasks.filter(completed=False).order_by('due_date')
    done_tasks = tasks.filter(completed=True).order_by('due_date')
    context = {
        'to_do_tasks': to_do_tasks,
        'done_tasks': done_tasks
    }
    return render(request, 'tasks/index.html', context)
