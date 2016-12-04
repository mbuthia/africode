from django.shortcuts import render, redirect

from account.form import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http.response import HttpResponse
from account.models import Category



# Create your views here.

def login_s(request):
    form=LoginForm(request.POST or None)
    if form.is_valid():
        email=form.cleaned_data.get('email')
        password=form.cleaned_data.get('password')
        try:
            user=User.objects.get(email=email)
            user= authenticate(username=user,password=password)
            if user is not None:
                if user.is_active:
                   login(request,user)
                  
                   return redirect('/')
                else:
                    messages.add_message(request,messages.INFO,'Your account is not active')
                    return redirect('/accounts/login')
            else:                  
                 messages.add_message(request,messages.INFO,'You provided invalid login credentials')
                 return redirect('/accounts/login')
 #return render(request,'login.html',{'message':'Please check you login credentials'})
        except User.DoesNotExist:
             messages.add_message(request,messages.INFO,'Your account does not exist')
             return redirect('/accounts/login')
           # return render(request,'login.html',{'message':'Your account does not exist'})
    return render(request,'login.html',{'category':Category.objects.all()})


def register(request):
    return render(request,'register.html',{'category':Category.objects.all()})

def logout_s(request):
    logout(request)
    return redirect('/')
def profile(request):
    return render(request,'profile.html',{'category':Category.objects.all()})
def reset(request):
    return render(request,'reset.html',{'category':Category.objects.all()})
@login_required()
def account_items_upload(request):
    return render(request,'upload.html',{'category':Category.objects.all()})