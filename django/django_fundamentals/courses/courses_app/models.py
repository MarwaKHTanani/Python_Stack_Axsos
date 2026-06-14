from django.db import models

# Create your models here.


class CourseManager(models.Manager):
    def validator(self, postData, course_id=None):
        errors = {}
        name = postData["name"].strip()
        description = postData["description"].strip()

        if len(name) < 5:
            errors["name"] = "course must be at least 5 character"
        if len(description) < 15:
            errors["description"] = "description must be at least 15 character"

        return errors


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=CourseManager()
