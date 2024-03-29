from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db import IntegrityError

from .forms import UserRegisterForm

from .models import CustomUser,Todo


def logoutUser(request):
    logout(request)
    return redirect('home')

def registerUser(request):

    # form = UserRegisterForm()

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
    
        try:
            user = CustomUser.objects.create(username=username,email=email)
            user.set_password(password)
            user.save()
            login(request,user)
        except IntegrityError:
            print("error message")
            return redirect('loginUser')
        return redirect('home')

    return render(request,'authform.html')

def loginUser(request):

    page = 'login'
    
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            print("No User")

        user = authenticate(request,username= email,password=password)
        if user:
            login(request,user)
            return redirect('home')
            
        else:
            print("No user..")
    context = {"page":page}   
    return render(request,'authform.html',context)
@login_required(login_url=loginUser)
def home(request):

    todos = Todo.objects.filter(user= request.user) if request.user.is_authenticated else []

    if request.method == "POST":
        todo = request.POST.get('todo')
        print("user is " ,request.user)
        todo_obj = Todo.objects.create(heading=todo,user=request.user)

    context = {'todos':todos}
    return render(request,'index.html',context)
@login_required(login_url=loginUser)
def deleteTodo(request,pk):

    todo = Todo.objects.get(id= pk)

    if todo:
        todo.delete()
        return redirect('home')

def forbidden(request):
    return render(request,'403.html')

def updateTodo(request,pk):
    page= "update"
    update_todo = Todo.objects.get(id = pk)

    if request.method == "POST":
        pass
    context = {
        "page":page,
        "value" : update_todo,
               }
    return render(request,'index.html',context) 