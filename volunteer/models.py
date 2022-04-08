from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


class Donation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    charity = models.ForeignKey("charity.Charity", on_delete=models.CASCADE, related_name="donations")
    price = models.FloatField()
    username = models.CharField(max_length=255)
    phone_number = PhoneNumberField()
    created_at = models.DateTimeField(auto_now_add=True)
    ioka_order_id = models.CharField(max_length=255)


class Volunteering(models.Model):
    charity = models.ForeignKey("charity.Charity", on_delete=models.CASCADE, related_name="volunteers")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    phone_number = PhoneNumberField()
    email = models.EmailField()
    city = models.CharField(max_length=50)
