from django.db import models
from datetime import date

# Create your models here.


class ShowManager(models.Manager):
    def validator(self, postData,show_id=None):
        errors = {}
        title = postData["title"].strip()
        network = postData["network"].strip()
        description = postData["description"].strip()
        related_date = postData["related_date"]
        existing_show=Show.objects.filter(title=title)

        if len(title) < 2:
            errors["title"] = "title should be at least 2 character"

        if show_id:
            existing_show=existing_show.exclude(id=show_id)
        if existing_show.exists():
            errors['title']='title already exists'

        if len(network) < 3:
            errors["network"] = "network should be at least 3 character"

        if description and len(description) < 10:
            errors["description"] = "description should be at least 10 character"

        if not related_date:
            errors["related_date"] = "release date is required"
        elif related_date >= str(date.today()):
            errors["related_date"] = "release date must be in the past"

        return errors


class Show(models.Model):
    title = models.CharField(max_length=100)
    network = models.CharField(max_length=50)
    related_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
