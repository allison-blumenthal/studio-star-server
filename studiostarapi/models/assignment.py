from django.db import models
from .user import User

class Assignment(models.Model):
  
  student_id = models.ForeignKey(User, on_delete=models.CASCADE)
  date = models.DateField()
