from django.db import models
from bboard.models import Bb
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Orders(models.Model):
    service = models.ManyToManyField(Bb)
    time = models.DateField(null=True, blank=True)

    # пользователь
    name = models.CharField(max_length=100)
    email_address = models.EmailField()
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=200)
    comment = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, db_index=True)