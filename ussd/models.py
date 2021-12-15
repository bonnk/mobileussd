from django.db import models
from datetime import datetime
# Create your models here.
class Bankaccount(models.Model):
    
    customerId = models.CharField(max_length=255, null=True)
    customerName = models.CharField(max_length=255)
    idnumber = models.CharField(max_length=255)
    balance = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=255)
    bankCode = models.CharField(max_length=255, null=True)
    locationOfBank = models.CharField(max_length=255)
    level  = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    created_on = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.phoneNumber


class Bankdetails(models.Model):
      customerId= models.CharField(max_length=255,null=True)
      phoneNumber= models.CharField(max_length=255)
      category= models.CharField(max_length=255)

      def __str__(self):
          return self.phoneNumber;
