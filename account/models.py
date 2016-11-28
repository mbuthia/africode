from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    
    def __str__(self):
        return self.name
    
    
    
class Account(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    facebook_id=models.CharField(max_length=80)
    google_id=models.CharField(max_length=80)
    address=models.CharField(max_length=80)
    city=models.CharField(max_length=80)
    counrty=models.CharField(max_length=80)
    zip_code=models.CharField(max_length=80)
    mobile=models.CharField(max_length=80)
    about_me=models.CharField(max_length=500)
    avatar=models.CharField(max_length=80)
    
    
    def __str__(self):
        return self.User.username
    

    
    

class Payment(models.Model):
    product_id = models.IntegerField()
    product_name=models.CharField(max_length=100)
    amount = models.IntegerField()
    payment_date = models.CharField(max_length=80)
    payment_type = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    deduction = models.IntegerField()
    net = models.IntegerField()
    status = models.IntegerField()
    
    def __str__(self):
        return self.product_name  
    
    
    
    
class Item(models.Model):
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    screen_shot = models.CharField(max_length= 100)
    file = models.CharField(max_length =500)
    demo = models.CharField(max_length=200)
    download = models.IntegerField()
    reviews = models.IntegerField()
    
    def __str__(self):
        return self.title
    
    
    
class Review(models.Model):
    item_id = models.ForeignKey(Item)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    review = models.CharField(max_length=500)
    rating = models.IntegerField()
    
    def __str__(self):
        return self.name