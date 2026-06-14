from django.shortcuts import render, redirect
from .models import User, Message, Comment
from django.contrib import messages
import bcrypt

# Create your views here.


def index(request):
    return render(request, "index.html")


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
    return redirect("/wall")

def login(request):
    user=User.objects.filter(email=request.POST['email'])
    if not user:
        messages.error(request,'invalid email or password')
        return redirect('/')
    user=user[0]
    if not bcrypt.checkpw(request.POST['password'].encode(),user.password.encode()):
        messages.error(request,'invalid email or password')
        return redirect('/')
    
    request.session['user_id']=user.id
    return redirect('/wall')

def logout(request):
    request.session.clear()
    return redirect('/')


def wall(request):
    if 'user_id' not in request.session:
        return redirect('/')
    
    context={
        'user':User.objects.get(id=request.session['user_id']),
        'messages':Message.objects.all().order_by('-created_at')
    }
    return render(request,'wall.html',context)


def create_message(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user =User.objects.get(id=request.session['user_id'])
    Message.objects.create(
        user=user,
        message=request.POST['message']
    )
    return redirect('/wall')


def create_comment(request,id):
    if 'user_id' not in request.session:
        return redirect('/')
    user=User.objects.get(id=request.session['user_id'])
    message=Message.objects.get(id=id)
    Comment.objects.create(
        user=user,
        message=message,
        comment=request.POST['comment']
    )
    return redirect('/wall')


def delete_message(request,id):
    message=Message.objects.get(id=id)
    
    if message.user.id==request.session['user_id']:
        message.delete()
    
    return redirect('/wall')
