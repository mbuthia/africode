from django.shortcuts import render,redirect
from account.models import Account, Category
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
from front.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User


from .form import ContactForm


def homepage(request):
    

    return render(request,'homepage.html',{'category':Category.objects.all()})
def about(request):
    return render(request,'about.html',{'category':Category.objects.all()})
@login_required()
def contact(request):
    if request.method =='POST':
        form_contact = ContactForm(request.POST or None)
        if form_contact.is_valid():
            email = form_contact.cleaned_data.get('email')
            message =form_contact.cleaned_data.get('message')
            content = Contact(
                email = email,
                message = message
            )
            messages.add_message(request, messages.INFO, 'message taken we will contact you soon')
            content.save()

    else:
        form_contact = ContactForm()
    return render(request,'contact.html',{'category':Category.objects.all(),'form':form_contact})