from django.db import models
from .user import User

class Studio(models.Model):
  
  name = models.CharField(max_length=50)
  teacher_id = models.ForeignKey(User, on_delete=models.CASCADE)

  
  @property
  def enrolled(self):
          return self.__chosen
  
  @enrolled.setter
  def enrolled(self, value):
          self.__chosen = value
