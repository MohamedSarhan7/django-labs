from django.shortcuts import render,HttpResponseRedirect
from .models import AuthMain
# Create your views here.

def index(req):
    return render(req, "base.html", {"test": "abc"})

def login(req):
    if req.method=='GET':
        return render(req, "authMain/login.html")
    ###############################################
    if req.POST['username'] and req.POST['password']:
        username = req.POST['username']
        password = req.POST['password']
        user=AuthMain.objects.filter(username=username, password=password)
        if len(user)>0:
            return HttpResponseRedirect('/course', {"username": username})
        return render(req, "authMain/login.html", {"err": "user not found or wrong password"})
    else:
        return render(req, "authMain/register.html", {"err": "All inputs are required"})

def register(req):
    if req.method == 'GET':
        return render(req, "authMain/register.html")
    ###############################################
    if req.POST['username'] and req.POST['password1'] and req.POST['password1']:
        username = req.POST['username']
        password = req.POST['password1']
        if password != req.POST['password2']:
            return render(req, "authMain/register.html", {"err": "password does not match"})
    
        AuthMain.objects.create(username=username, password=password)
        return HttpResponseRedirect('/course', {"username": username})
    else:
        return render(req, "authMain/register.html", {"err": "All inputs are required"})

def logout(req):
    return HttpResponseRedirect("/")
