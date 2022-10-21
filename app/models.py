from django.db import models

# Create your models here.

class Garden(models.Model):
    name=models.CharField(max_length=100)
    Email_name=models.EmailField(max_length=100)
    subject_name=models.CharField(max_length=100)
    message=models.TextField(max_length=250)
    
    
    