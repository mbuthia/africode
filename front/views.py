from django.shortcuts import render
from account.models import Account, Category
from django.http.response import HttpResponse

# Create your views here.
def homepage(request):
    

    return render(request,'homepage.html',{'category':Category.objects.all()})
def about(request):
    return render(request,'about.html',{'category':Category.objects.all()})
def contact(request):
    return render(request,'contact.html',{'category':Category.objects.all()})