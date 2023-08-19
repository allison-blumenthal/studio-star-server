from django.db import models

class Sticker(models.Model):
  
  unicode = models.CharField(max_length=10)
