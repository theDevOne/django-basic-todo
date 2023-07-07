from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

from .models import TodoItem
from .forms import TodoItemForm, UserLoginForm, UserRegisterForm

User = get_user_model()

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            username = form.cleaned_data["username"]
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password,
            )
            user.is_active = True
            user.save()
            login(request,user)
            return redirect("/")
    else:
        form = UserRegisterForm()
    
    return render(request, "todolist/register.html", {"form": form })

def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            form.add_error(None, "Invalid username or password.")
    else:
        form = UserLoginForm()
    return render(request, 'todolist/login.html', {'form': form})

@login_required()
def logout_user(request):
    logout(request)
    return redirect("/")

class TodoListView(LoginRequiredMixin,ListView):
    model = TodoItem
    paginate_by = 2 
    context_object_name = 'todos'
    template_name = 'todolist/todo_list.html'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user).order_by("id")

@login_required()
def view_todo_item(request,pk):
    try:
        todo_item = TodoItem.objects.get(pk=pk,user=request.user)
    except TodoItem.DoesNotExist:
        return render(request, 'todolist/404.html')

    return render(request, 'todolist/view_todo_item.html', {'todo': todo_item})

@login_required()
def create_todo_item(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            todo_item = form.save(commit=False)
            todo_item.user = request.user
            todo_item.save()
            return redirect('/')
    else:
        form = TodoItemForm()
    return render(request, 'todolist/create_todo_item.html', {'form': form})



@login_required()
def edit_todo_item(request, pk):
    try:
        todo_item = TodoItem.objects.get(pk=pk,user=request.user)
    except TodoItem.DoesNotExist:
        return render(request, 'todolist/404.html')

    if request.method == 'POST':
        form = TodoItemForm(request.POST, instance=todo_item)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoItemForm(instance=todo_item)
    return render(request, 'todolist/edit_todo_item.html', {'form': form })

@login_required()
def delete_todo_item(request, pk):
    try:
        todo = TodoItem.objects.get(pk=pk,user=request.user)
        todo.delete()
    except TodoItem.DoesNotExist:
        return render(request, 'todolist/404.html')
    return redirect("/")


