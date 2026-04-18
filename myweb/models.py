
# Create your models here.
<<<<<<< HEAD
class Task(models.Model):
  title = models.CharField(max_length=200)
  created_at = models.DateTimeField(auto_now_add=True)
  def__str__(self):
        return self.title
=======


from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

    college_id = models.CharField(max_length=20)
    semester = models.CharField(max_length=10)
    phone_no = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
>>>>>>> df91bc5 (added registration logic and student data fields)
