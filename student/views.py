from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import Student
# Create your views here.



def index(req):
    students = Student.objects.all()
    print(students)
    return render(req,"student/index.html",{"students":students})

def add(req):
    return render(req,"student/add-student.html",{"test":"abc"})

def update(req,id):
    return HttpResponseRedirect("/student")


def delete(req,id):
    return HttpResponseRedirect("/student")
