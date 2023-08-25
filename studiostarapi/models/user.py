from django.db import models


class User(models.Model):

    uid = models.CharField(max_length=100)
    is_teacher = models.BooleanField(default=False)
    instrument = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    pronouns = models.CharField(max_length=50)
    birthdate = models.DateField(null=True)
    guardian_names = models.CharField(max_length=300, null=True)
    email = models.CharField(max_length=100)
    profile_image_url = models.CharField(max_length=5000)
