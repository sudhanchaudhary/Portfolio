import requests

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.core.exceptions import ValidationError
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    project=Projects.objects.all()
    frontend=Frontend.objects.all()
    backend=Backend.objects.all()
    tools=Tools.objects.all()
    github_contribution='https://ghchart.rshah.org/sudhanchaudhary'
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        Message.objects.create(name=name,email=email,message=message)
        messages.success(request,'Thanks for the message')
        return redirect('home')
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
            return redirect('home')
        else:
            messages.error(request,'username or password is invalid!!')
    return render(request,'account/login.html')
@login_required(login_url='login')
def content(request):
    msg=Message.objects.all()
    project=Projects.objects.all()
    backend=Backend.objects.all()
    frontend=Frontend.objects.all()
    tools=Tools.objects.all()
    if request.method == "POST":
        p_name=request.POST.get('p_title')
        p_desc=request.POST.get('p_desc')
        p_tech=request.POST.get('p_tech')
        g_link=request.POST.get('g_link')
        l_link=request.POST.get('l_link')
        Projects.objects.create(title=p_name,desc=p_desc,tech=p_tech,github_link=g_link,live_link=l_link)
        return redirect('context')
    context={
        'msg':msg,
        'project':project,
        'backend':backend,
        'frontend':frontend,
        'tools':tools
    }
    return render(request,'account/content.html',context)

    