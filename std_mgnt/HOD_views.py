from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required



@login_required(login_url='/')
def hodPanel(request):
    return render(request,'HOD/home.html')


@login_required(login_url='/')
def addStudent(request):
    return render(request,'HOD/addStudent.html')
