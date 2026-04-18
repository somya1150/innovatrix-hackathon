
# Create your models here.


from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    # This links the profile to a specific user
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Your campus-specific fields
    college_id = models.CharField(max_length=20)
    semester = models.CharField(max_length=10)
    phone_no = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
