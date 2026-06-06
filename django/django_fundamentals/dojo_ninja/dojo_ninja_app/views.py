from django.shortcuts import redirect, render

from .models import Dojo, Ninja
# Create your views here.


def index(request):
    context = {"dojos": Dojo.objects.all()}
    return render(request, "index.html", context)


def create_dojo(request):
    if request.method == "POST":
        Dojo.objects.create(
            name=request.POST["name"],
            city=request.POST["city"],
            state=request.POST["state"],
        )
    return redirect("/")


def create_ninja(request):
    if request.method == "POST":
        dojo = Dojo.objects.get(id=request.POST["dojo"])
        Ninja.objects.create(
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            dojo=dojo,
        )
    return redirect("/")

def delete_dojo(request,id):
    if request.method=='POST':
        dojo=Dojo.objects.get(id=id)
        dojo.delete()
    return redirect("/")