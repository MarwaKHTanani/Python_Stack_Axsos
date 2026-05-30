from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    if "counter" in request.session:
        request.session["counter"] += 1
    else:
        request.session["counter"] = 1
    context = {
        "counter": request.session["counter"]
    }

    return render(request, "index.html",context)


def destroy_session(request):
    if "counter" in request.session:
        del request.session["counter"]
    return redirect("/")


def plus2(request):
    
    request.session["counter"] += 1
    return redirect("/")
