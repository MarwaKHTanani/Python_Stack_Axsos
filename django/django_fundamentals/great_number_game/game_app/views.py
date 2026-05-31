from django.shortcuts import render, redirect
import random
# Create your views here.


def index(request):
    if "number" not in request.session:
        request.session["number"] = random.randint(1, 100)
        request.session["attempts"] = 0

    context = {
        "message": request.session.get("message"),
        "correct": request.session.get("correct", False),
        "attempts": request.session.get("attempts", 0),
    }

    return render(request, "index.html", context)


def guess(request):
    if request.POST["guess"] == "":
        request.session["message"] = "Please enter a number!"
        request.session["correct"] = False
        return redirect("/")

    guess = int(request.POST["guess"])

    request.session["attempts"] += 1

    if guess < request.session["number"]:
        request.session["message"] = "Too low!"
        request.session["correct"] = False

    elif guess > request.session["number"]:
        request.session["message"] = "Too high!"
        request.session["correct"] = False

    else:
        request.session["message"] = f"{request.session['number']} was the number!"
        request.session["correct"] = True

    return redirect("/")


def reset(request):
    request.session.clear()
    return redirect("/")