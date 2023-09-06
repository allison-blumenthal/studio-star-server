from django.db import models
from .assignment import Assignment

class Task(models.Model):
  
  assignment_id = models.ForeignKey(Assignment, on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  description = models.TextField()
  sticker_goal = models.IntegerField()
  current_stickers = models.IntegerField(default=0)
  is_completed = models.BooleanField(default=False)
