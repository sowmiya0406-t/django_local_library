from django.shortcuts import render,redirect
from .models import Todo

# Create a new Todo
def create_todo(request):
    if request.method == 'POST':
        task = request.POST['task']
        Todo.objects.create(task=task)
        return redirect('list_todos')
    return render(request, 'todo/create_todo.html')

# List all Todos
def list_todos(request):
    todos = Todo.objects.all()
    return render(request, 'todo/list_todos.html', {'todos': todos})

# Update a Todo
def update_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        todo.task = request.POST['task']
        todo.completed = 'completed' in request.POST
        todo.save()
        return redirect('list_todos')
    return render(request, 'todo/update_todo.html', {'todo': todo})

# Delete a Todo
def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('list_todos')