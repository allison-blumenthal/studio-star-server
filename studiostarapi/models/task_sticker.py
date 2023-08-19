from django.db import models
from .task import Task
from .sticker import Sticker

class TaskSticker(models.Model):
  
  task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
  sticker_id = models.ForeignKey(Sticker, on_delete=models.CASCADE)
