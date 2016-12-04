from django.contrib import admin
from account.models import Category, Item, Account, Review, Payment

# Register your models here.
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Account)
admin.site.register(Review)
admin.site.register(Payment)
