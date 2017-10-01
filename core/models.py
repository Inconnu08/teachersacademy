from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from .managers import UserManager


class User(AbstractUser):
    username = models.CharField(max_length=30, null=True, blank=True)
    phone = models.CharField(max_length=20, validators=[
        RegexValidator(regex=r'^\+?8801?\d{9}$',
                       message="Phone number must be entered in the format: '+8801*********'")
    ], blank=False, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    EMAIL_FIELD = 'email'

    def __str__(self):
        return self.get_full_name() or self.phone

    def get_absolute_url(self):
        return reverse('user-details', kwargs=self.pk)
