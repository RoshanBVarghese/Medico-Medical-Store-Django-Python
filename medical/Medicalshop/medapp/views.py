from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import MedicalForm
from .models import Medicines
import re

# Create your views here
@login_required(login_url='login')
def Homepage(request):
    return render(request,'base.html')

def Signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if not (uname and email and pass1):
            messages.error(request,"Please fill all the fields")
            return redirect('signup')
        if User.objects.filter(username=uname).exists():
            messages.error(request,"Username already exists")
            return redirect('signup')
        if User.objects.filter(email=email).exists():
            messages.error(request,"Email already exists")
            return redirect('signup')
        
        if not re.match('[a-zA-Z0-9@#]',pass1) or len(pass1)!=6:
            messages.error(request,"Passwords must contain alphabets, numbers,symbols and must contain 6 letters")
            return redirect('signup')

        if pass1!=pass2:
            messages.error(request,"Passwords arent same!!")
            return redirect('signup')
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render(request,'signup.html')


def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('base')
        else:
            messages.error(request,"invalid username or password")
            return redirect('login')
        
    return render(request,'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')

# Medicine list

@login_required(login_url='login')
def Meds(request):
    form=MedicalForm()
    if request.method== 'POST':
        form=MedicalForm(request.POST)
        form.save()

    data=Medicines.objects.all()
    context={
        'form':form,
        'data':data,
    }
    return render(request,'meds.html',context)



# Delete view

def Delete_record(request,id):
    a=Medicines.objects.get(pk=id)
    a.delete()
    return redirect('meds')

# Update view

def Update_record(request,id):
    if request.method=='POST':
        data=Medicines.objects.get(pk=id)
        form=MedicalForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
    else:
        data=Medicines.objects.get(pk=id)
        form=MedicalForm(instance=data) 
    context={
        'form':form,
    }
    return render(request,'update.html',context)

# Add View
@login_required(login_url='login')
def Add(request):
    form=MedicalForm()
    if request.method== 'POST':
        form=MedicalForm(request.POST)
        form.save()

    context={
        'form':form,
    }
    return render(request,'add.html',context)

# Searchbar
@login_required(login_url='login')
def Searchbar(request):
    if request.method=='GET':
        search=request.GET.get('search')
        name = Medicines.objects.filter(name__istartswith=search)
        return render(request,'search.html',{'name':name})