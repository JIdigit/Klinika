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
    image = models.ImageField(upload_to='clinics/%Y/%m/%d', max_length=200, blank=True, default='noimage.png' )
    phone_number = PhoneField(blank=True, help_text='Contact phone number')

    def __str__(self):
        return self.name




class Profile(AbstractUser):
    CHOICE = [
        ('doctor', 'Doctor'),
        ('client', 'Client')
    ]
    PROFESSION = [
        ('эндокринолог', 'Эндокринолог'),
        ('кардиологог', 'Кардиолог')
    ]
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name='doctor_set')
    description = models.TextField(blank=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    profession = models.CharField(max_length=50, choices=PROFESSION,blank=True)
    image = models.ImageField(upload_to='doctors/%Y/%m/%d', max_length=200, default='deafult.jpg')
    type = models.CharField(max_length=10, choices=CHOICE)


    def __str__(self):
        return self.first_name


class Comments(models.Model):
    comments = models.ForeignKey(Profile, related_name='comments' ,on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100, default='Anonymous')
    text = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.nickname


class Ocenka(models.Model):
    CHOICE = [
        (1, 'one'),
        (2, 'two'),
        (3, 'three'),
        (4, 'four'),
        (5, 'five')
    ]
    likes = models.ForeignKey(Profile, related_name='evaluations', on_delete=models.CASCADE)
    ocenka = models.PositiveIntegerField(choices=CHOICE, default=None)


class Appointments(models.Model):
    pass

