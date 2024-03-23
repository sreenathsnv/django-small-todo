from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse

from .forms import UserForm

from .models import CustomUser,Todo


def loginUser(request):

    form = UserForm()
    # if request.user.is_authenticated:
    #     return redirect('home')
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            pass

        user = authenticate(request,username= email,password=password)
        if user:
            login(user)
            context = {}
            
            return redirect('home')
        else:
            pass
        
    return render(request,'authform.html',{"form":form})

def home(request):

    todos = Todo.objects.all()

    if request.method == "POST":
        todo = request.POST.get('todo')
        print("user is " ,request.user)
        todo_obj = Todo.objects.create(heading=todo,user=request.user)
    context = {'todos':todos}
    return render(request,'index.html',context)