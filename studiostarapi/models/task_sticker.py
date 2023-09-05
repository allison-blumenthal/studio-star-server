from django.db import models
from .task import Task
from .sticker import Sticker

class TaskSticker(models.Model):
  
  task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
  sticker_id = models.ForeignKey(Sticker, on_delete=models.CASCADE)
  
  # function to update the number of task_stickers associated with the task # and set is_completed to True if the goal has been met 
  def update_task_current_stickers(self):
    task = self.task_id
    total_stickers = TaskSticker.objects.filter(task_id=task).count()
    task.current_stickers = total_stickers
    
    if task.current_stickers >= task.sticker_goal:
      task.is_completed = True
    else:
      task.is_completed = False
    
    task.save()
