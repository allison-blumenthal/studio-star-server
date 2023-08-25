from django.db import models
from .user import User
from .studio import Studio

class StudioStudent(models.Model):
  
  student_id = models.ForeignKey(User, on_delete=models.CASCADE)
  studio_id = models.ForeignKey(Studio, on_delete=models.CASCADE)
