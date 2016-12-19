from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Contact(models.Model):
    email = models.EmailField(max_length=100)
    message = models.CharField(max_length=250)

