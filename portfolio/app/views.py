import requests

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.core.exceptions import ValidationError
from django.contrib import messages
from .models import *

# Create your views here.
def home(request):
    project=Projects.objects.all()
    frontend=Frontend.objects.all()
    backend=Backend.objects.all()
    tools=Tools.objects.all()
    github_contribution='https://ghchart.rshah.org/sudhanchaudhary'
    context={
        'project':project,
        'frontend':frontend,
        'backend':backend,
        'tools':tools,
        'github_contrib':github_contribution
    }
    return render(request,'home.html',context)

def log_in(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if not user is None:
            login(request,user)
        else:
            messages.error(request,'username or password is invalid!!')
    return render(request,'account/login.html')