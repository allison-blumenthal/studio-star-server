from django.db import models
from .user import User

class TeacherStudent(models.Model):
  
  teacher_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher_relationships')
  student_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_relationships')
  
  class Meta:
    unique_together = ('teacher', 'student')
