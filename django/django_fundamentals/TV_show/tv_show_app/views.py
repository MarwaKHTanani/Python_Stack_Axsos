from django.shortcuts import render, redirect
from tv_show_app.models import Show
from django.contrib import messages


# Create your views here.
def redirect_to_shows(request):
    return redirect("/shows")


def shows(request):
    context = {"all_shows": Show.objects.all()}
    return render(request, "shows.html", context)


def new_show(request):
    return render(request, "new_show.html")


def create_show(request):
    errors = Show.objects.validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/shows/new")

    show = Show.objects.create(
        title=request.POST["title"],
        network=request.POST["network"],
        related_date=request.POST["related_date"],
        description=request.POST["description"],
    )

    return redirect(f"/shows/{show.id}")


def edit_show(request, show_id):
    context = {"show": Show.objects.get(id=show_id)}
    return render(request, "edit_show.html", context)


def details_show(request, show_id):
    context = {"show": Show.objects.get(id=show_id)}
    return render(request, "show_details.html", context)


def delete_show(request, show_id):
    show = Show.objects.get(id=show_id)
    show.delete()

    return redirect("/shows")


def update_show(request, show_id):
    errors = Show.objects.validator(request.POST,show_id)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/shows/{show_id}/edit")
    
    show = Show.objects.get(id=show_id)

    show.title = request.POST["title"]
    show.network = request.POST["network"]
    show.related_date = request.POST["related_date"]
    show.description = request.POST["description"]

    show.save()
    return redirect(f"/shows/{show.id}")
