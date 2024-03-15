from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse

from .models import CustomUser

def test(request):
    return HttpResponse("Joseph is a PDF")


def loginUser(request):

    if request.user.is_authenticated:
        return 
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
            # return redirect()
        else:
            pass
        
        

