from django.db import models
from .task import Task
from .sticker import Sticker

class TaskSticker(models.Model):
  
  task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
  sticker_id = models.ForeignKey(Sticker, on_delete=models.CASCADE)
  
  # function to update the number of task_stickers associated with the task 
  def update_task_current_stickers(self):
    task = self.task_id
    total_stickers = TaskSticker.objects.filter(task_id=task).count()
    task.current_stickers = total_stickers
    task.save()
