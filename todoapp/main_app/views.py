from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView
)
from .models import Make_ToDo

def main(request):
    context = {
        'todo': Make_ToDo.objects.all()
    }
    return render(request, 'blog/base.html', context)
    
class ToDoListView(ListView):
    model = Make_ToDo
    template_name = 'main_app/index.html'
    context_object_name = 'todo'

class ToDoCreateView(CreateView):
    model = Make_ToDo
    template_name = 'main_app/add.html'
    context_object_name = 'todo'
    fields = [
        'task_name',
        'status'
    ]
    success_url = '/'

def delete_todo(request, todo_id):
    to_delete = Make_ToDo.objects.get(id=todo_id)
    to_delete.delete()
    return redirect("/")