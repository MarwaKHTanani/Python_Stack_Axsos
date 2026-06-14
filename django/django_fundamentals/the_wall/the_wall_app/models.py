from django.db import models
import re

# Create your models here.


class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        first_name = postData.get("first_name", "").strip()
        last_name = postData.get("last_name", "").strip()
        email = postData.get("email", "").strip()
        password = postData.get("password", "").strip()
        EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")

        if len(first_name) < 2:
            errors["first_name"] = "first name should be at least  character"
        if len(last_name) < 2:
            errors["last_name"] = "last name should be at least 2 character"
        if not EMAIL_REGEX.match(email):
            errors["email"] = "invalid email format"
        elif User.objects.filter(email=email).exists():
            errors["email"] = "email already exist"
        if len(password) < 6:
            errors["password"] = "password should be at least 6 character"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=UserManager()


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(
        Message, on_delete=models.CASCADE, related_name="comments"
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
