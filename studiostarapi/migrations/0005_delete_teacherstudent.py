# Generated by Django 4.1.3 on 2023-08-25 01:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studiostarapi', '0004_studio_studiostudent'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TeacherStudent',
        ),
    ]