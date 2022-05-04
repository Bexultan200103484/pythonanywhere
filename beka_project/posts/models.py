from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator

# Create your models here.
class RegUser(models.Model):
    firstname = models.CharField(max_length=255, verbose_name="First name")
    lastname = models.CharField(max_length=255, verbose_name="Last name")
    user_id = models.PositiveIntegerField(primary_key=True, default=1)
    GChoices = (('M', 'Male'), ('F', 'Female'),)
    gender = models.CharField(max_length=1, choices=GChoices)
    email = models.EmailField(validators=[MinLengthValidator(10)])
    username = models.CharField(max_length=255, verbose_name="Username")
    password = models.CharField(max_length=255)