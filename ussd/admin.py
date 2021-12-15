from django.contrib import admin
from .models import *    #import all models
# Register your models here.

class BankdaccountAdmin (admin.ModelAdmin):
    list_display =['customerId', 'customerName','balance']
    search_fields =['customerId','customerName','balance']


class BankdetailsAdmin (admin.ModelAdmin):
     list_display =['customerId', 'category']
     search_fields =['CustomerId','category']

admin.site.register(Bankaccount, BankdaccountAdmin)
admin.site.register(Bankdetails, BankdetailsAdmin)
