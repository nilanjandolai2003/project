from django.shortcuts import render,HttpResponse
from .models import student,Role,department
from datetime import datetime
from .forms import student_form

# Create your views here.
def index(request):
    return render(request,'index.html')
def all_members(request):
    students=student.objects.all()
    context={
        'st':students
    }
    return render(request,'all_members.html',context)
def add_members(request):
    if request.method=='POST':
        form=student_form(request.POST)
        if form.is_valid():
            form.save()
            
            return HttpResponse('member added successfully')
    else:
        form=student_form()
    return render(request,'add_members.html',{'form':form})
def filter_members(request):
    return render(request,'filter_members.html')
            