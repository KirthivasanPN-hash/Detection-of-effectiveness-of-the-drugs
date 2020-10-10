from django.db import models

# Create your models here.

class Report(models.Model):

    Name = models.CharField(max_length=100)
    Email_id = models.CharField(max_length=100)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=100)
    Mobilenumber = models.IntegerField()
    Aadharnumber = models.IntegerField()
    Address = models.TextField()
    img = models.ImageField(upload_to='pics')

