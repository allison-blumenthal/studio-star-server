from django.db import models
from .user import User

class TeacherStudent(models.Model):
  
  teacher_id = models.ForeignKey(User, on_delete=models.CASCADE)
  student_id = models.ForeignKey(User, on_delete=models.CASCADE)
