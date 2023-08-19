from django.db import models


class User(models.Model):

    uid = models.CharField(max_length=100)
    is_teacher = models.BooleanField()
    instrument = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    pronouns = models.CharField(max_length=50)
    birthdate = models.DateField()
    guardian_names = models.CharField(max_length=300)
    email = models.CharField(max_length=100)
    profile_image_url = models.CharField(max_length=5000)
    
