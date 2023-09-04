from django.db import models
from .assignment import Assignment
from .task_sticker import TaskSticker

class Task(models.Model):
  
  assignment_id = models.ForeignKey(Assignment, on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  description = models.TextField()
  sticker_goal = models.IntegerField()
  current_stickers = models.IntegerField(default=0)
  is_completed = models.BooleanField(default=False)
  
  # function to update the number of task_stickers associated with the task 
  def update_current_stickers(self):
    total_stickers = TaskSticker.objects.filter(task_id=self.id).aggregate(total=models.Sum('sticker_count'))['total'] or 0
    self.current_stickers = total_stickers
    self.save()
