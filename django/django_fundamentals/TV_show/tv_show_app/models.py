from django.db import models

# Create your models here.

class Show(models.Model):
    title=models.CharField(max_length=100)
    network=models.CharField(max_length=50)
    related_date=models.DateField()
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    