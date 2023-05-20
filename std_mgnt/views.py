from django.shortcuts import render,redirect, HttpResponse
from app.EmailBackend import EmailBackend
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from app.models import CostumUser




def home(request):
    return render(request,'base.html')

def LOGIN(request):
    return render(request,'login.html')

def doLogin(request):
    if request.method== 'POST':
        user = EmailBackend.authenticate(request,username = request.POST.get('email'), password=request.POST.get('password'))
        
        if user!=None:
            user_type=user.user_type
            login(request,user)
           
            if user_type == "1":
                return redirect('HODhome')
            elif user_type == "2":
                return HttpResponse("Welcome to HOD Pannel")
            elif user_type == "3":
                return HttpResponse("Welcome to HOD Pannel")
            else:
                messages.error(request,"Email and password are invalid")
                return redirect('login')
        else:
            messages.error(request,"Email and password are invalid")
            return redirect('login')
        
def doLogOut(request):
    logout(request)
    return redirect('login')


def profile(request):
    user = CostumUser.objects.get(id = request.user.id)
    context ={
        "user":user
    }
    return render(request,'profile.html',context)

def profileUpdate(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        profile_pic = request.FILES.get('profile_pic')
        # email= request.POST.get('email')
        password= request.POST.get('password')
        # username= request.POST.get('username')
        # print(profile_pic)

        try:
            custumuser = CostumUser.objects.get(id = request.user.id)

            custumuser.first_name = first_name
            custumuser.last_name = last_name

            if password !=None and password !="":
                custumuser.set_password(password)
            if profile_pic !=None and profile_pic !="":
                custumuser.profile_pic = profile_pic

            custumuser.save()
            messages.success(request,'Profile Updated Succesfull')
           
            return redirect('profile')
        except:
             messages.error(request,"Update Failed")
    return render(request,'profile.html')
