from django.shortcuts import redirect, render, get_object_or_404
from .models import todo
from .forms import todoAddForm, todoUpdateForm


def home(request):
    return render(request, 'todo/home.html')

def todo_list(request):
    todos = todo.objects.all()
    form = todoAddForm()
    if request.method == "POST":
        form = todoAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {
        'todos': todos,
        'form': form
    }
    return render(request, "todo/todo_list.html", context)

def todo_add(request):
    form = todoAddForm()
    if request.method == "POST":
        form = todoAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {
        'form': form
    }
    return render(request, "todo/todo_add.html", context)

def todo_update(request, id):
    # Todo = todo.objects.get(id=id)
    Todo = get_object_or_404(todo, id=id)
    form = todoUpdateForm(instance=Todo)
    if request.method == "POST":
        form = todoUpdateForm(request.POST, instance=Todo)
        if form.is_valid:
            form.save()
            return redirect('list')
    context = {
        'form': form,
        'Todo': Todo,
    }
    return render(request, "todo/todo_update.html", context)

def todo_delete(request, id):
    Todo = get_object_or_404(todo, id=id)
    if request.method == "POST":
        Todo.delete()
        return redirect('list')
    context = {
        'Todo': Todo
    }
    return render(request, "todo/todo_delete.html", context)
