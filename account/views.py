from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'login.html',{})


## register call view
def register(request):
    return render(request,'register.html',{})