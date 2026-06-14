from urllib import request

from django.shortcuts import render, redirect
from login_register.models import User
from django.contrib import messages
import bcrypt

# Create your views here.


def index(request):
    return render(request, "index.html")


def login(request):
    
    user = User.objects.filter(email=request.POST["email"])

    if not user:
        messages.error(request, "invalid email or password")
        return redirect("/")
    user = user[0]
    if not bcrypt.checkpw(request.POST["password"].encode(), user.password.encode()):
        messages.error(request, "invalid email or password")
        return redirect("/")
    request.session["user_id"] = user.id
    request.session['operation'] = 'logged in'

    return redirect("/success")


def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")

    password = request.POST["password"].strip()
    hash_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    user = User.objects.create(
        first_name=request.POST["first_name"].strip(),
        last_name=request.POST["last_name"].strip(),
        email=request.POST["email"].strip(),
        password=hash_pw,
    )
    request.session["user_id"] = user.id
    request.session['operation'] = 'registered'
    return redirect("/success")


def success_page(request, operation=None):
    if 'user_id' not in request.session:
        return redirect('/')

    context={
        'user':User.objects.get(id=request.session['user_id']),
        'operation': request.session.get('operation')
    }
    return render(request,'success.html',context)


def logout(request):
    request.session.clear()
    return redirect('/')
