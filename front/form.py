from django import forms


class ContactForm(forms.Form):
    email = forms.CharField(label='Email', max_length=200,
                            widget=forms.EmailInput(attrs={
                                'class': 'form-control'
                            }))
    message = forms.CharField(label='Message',widget=forms.Textarea(attrs={'rows':10,'cols':50,
                                                                           'class':'form-control'
                                                                           }),
                              required = True)
