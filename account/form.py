from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields={
            'email',
            'password'
            }
        
class RegisterForm(forms.Form):
    firstname = forms.CharField(label='Firstname', max_length=100,
                               widget= forms.TextInput(attrs={
                                   'class':'form-control'
                               }))
    lastname = forms.CharField(label = 'Lastname', max_length=100,
                               widget = forms.TextInput(attrs={
                                   'class':'form-control',

                               }))
    email =forms.CharField(label='Email',max_length=200,
                           widget=forms.EmailInput(attrs={
                               'class':'form-control'
                           }))
    password =forms.CharField(label='Password',max_length=100,
                              widget =forms.PasswordInput(attrs={
                                  'class':'form-control'
                              }))
    confirm_password=forms.CharField(label='Confirm Password',max_length=100,
                                     widget=forms.PasswordInput(attrs={
                                         'class':'form-control'
                                     }))


     