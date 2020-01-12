from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import  AbstractUser, User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Clinic(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    address = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='clinics/%Y/%m/%d', max_length=200, blank=True)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')

    def __str__(self):
        return self.name


class Doctor(AbstractUser):
    CHOICE = [
        ('doctor', 'Doctor'),
        ('client', 'Client')
    ]
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name='doctor_set')
    # name = models.CharField(max_length=100)
    # surname = models.CharField(max_length=100, blank=True)
    # slug = models.SlugField(max_length=100, unique=True, blank=True)
    type
    description = models.TextField(blank=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    profession = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='doctors/%Y/%m/%d', max_length=200, default='deafult.jpg')
    type = models.CharField(max_length=10, choices=CHOICE)
    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Doctor.objects.create(user=instance)
    #
    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.doctor.save()

    def __str__(self):
        return self.first_name




class Comments(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100, default='Anonymous')
    text = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)