from django.db import models
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null = True, blank = True, on_delete=models.SET_NULL)
    device_id = models.CharField(max_length = 300, null = True, blank = True)
    profile_picture = models.ImageField(null=True)
    first_name = models.CharField(max_length = 250, null = True)
    last_name = models.CharField(max_length = 250, null = True)
    email = models.EmailField(max_length = 250, null = True, blank = True)
    address_line_1 = models.CharField(max_length = 250, null = True)
    address_line_2 = models.CharField(max_length = 250, null = True, blank = True)
    city = models.CharField(max_length = 250, null = True)
    state = models.CharField(max_length = 250, null = True)
    country = models.CharField(max_length = 250, default = "Nigeria")
    postal_code = models.PositiveIntegerField(null = True)
    phone_number = PhoneNumberField()


    def __str__(self):
        if self.user:
            name = self.user.username
        else:
            name = self.device_id
        return str(name)



class Address(models.Model):
    first_name = models.CharField(max_length = 250, null = True)
    last_name = models.CharField(max_length = 250, null = True)
    email = models.EmailField(max_length = 250, null = True, blank = True)
    state = models.CharField(max_length = 250, null = True)
    city = models.CharField(max_length=100,null = True)
    country = models.CharField(null = True, max_length = 250, default = "Nigeria")
    phone = models.CharField(null = True,max_length=20)
    address_line_1 = models.CharField(max_length=250,null = True)
    address_line_2 = models.CharField(max_length=250,null = True, blank = True)
    customer  = models.ForeignKey(Customer, related_name="+", null = True,   on_delete = models.SET_NULL)
    class Meta:
        verbose_name: str = ' Delivery Address'
        verbose_name_plural: str = ' Delivery Addresses'

    def __str__(self):
        return self.state.__str__()
        

#class DeliveryAddress(models.Model):
#   customer = models.ForeignKey(Customer, null = True, on_delete = models.SET_NULL)
#   first_name = models.CharField(max_length = 250, null = True)
#  last_name = models.CharField(max_length = 250, null = True)
#   email = models.EmailField(max_length = 250, null = True, blank = True)
#   phone_number = models.PositiveIntegerField(null = True)
#  address = models.ForeignKey(Address, related_name='shipping_address', null = True, on_delete = models.CASCADE)

