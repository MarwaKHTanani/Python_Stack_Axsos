from django.db import models

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=100)
    desc=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Authors(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    notes = models.TextField(default="No Notes")
    books=models.ManyToManyField(Book, related_name='authors')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    