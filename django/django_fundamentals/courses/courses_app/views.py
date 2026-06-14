from django.shortcuts import render, redirect
from courses_app.models import Course
from django.contrib import messages

# Create your views here.


def index(request):
    context = {"all_courses": Course.objects.all()}
    return render(request, "index.html", context)


def create_course(request):
    errors = Course.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
        
    Course.objects.create(
        name=request.POST["name"].strip(),
        description=request.POST["description"].strip(),
    )

    return redirect("/")


def delete_page(request, course_id):
    context = {"course": Course.objects.get(id=course_id)}
    return render(request, "delete.html", context)


def destroy(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    return redirect("/")
