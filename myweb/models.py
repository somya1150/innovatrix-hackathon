
# Create your models here.
# created a model for login page then makemigrations and migrate it to the database. and then registered it in admin.py file to view it in
#  the admin panel.

from django.db import models
from django.contrib.auth.models import User

class login(models.Model):
    username= models.CharField(max_length=122)
    email =models.CharField(max_length=122)
    college_id=models.CharField(max_length=122)
    sem=models.CharField(max_length=122)
    phone =models.CharField(max_length=12)
    password=models.CharField(max_length=122)

def __str__(self):
    return self.username