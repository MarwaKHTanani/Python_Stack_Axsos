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
        confirm_pw=postData.get('confirm_pw','').strip()
        EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")

        if len(first_name) < 2 or not first_name.isalpha():
            errors["first_name"] = (
                "first name should be at least 2 character and only letters"
            )

        if len(last_name) < 2 or not last_name.isalpha():
            errors["last_name"] = (
                "last name should be at least 2 character and only letters"
            )

        if not EMAIL_REGEX.match(email):
            errors["email"] = "invalid email format"
            
        elif User.objects.filter(email=email).exists():
            errors['email']='email already exist'
    
        if len(password) < 8:
            errors["password"] = "password must be at least 8 character"
        
        if confirm_pw != password:
            errors["confirm_pw"]='password do not match'
        
        
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
