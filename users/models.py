from django.contrib.auth.models import AbstractUser
from django.db import models
from phone_field import PhoneField


class Clients(AbstractUser):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)

    CHOICE = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    sex = models.CharField(max_length=7, choices=CHOICE, blank=True)
    date_of_birth = models.DateTimeField(blank=True)
    phone_number = PhoneField()




