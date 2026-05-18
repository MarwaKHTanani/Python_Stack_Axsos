from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "kjh5555"


@app.route("/")
def index():
    if "number" not in session:
        session["number"] = random.randint(1, 100)
        session["attempts"] = 0
    return render_template(
        "index.html",
        message=session.get("message"),
        correct=session.get("correct", False),
    )


@app.route("/guess", methods=["POST"])
def guess():
    if request.form["guess"] == "":
        session["message"] = "Please enter a number!"
        session["correct"] = False
        return redirect("/")
    
    guess = int(request.form["guess"])
    session["attempts"] += 1
    if guess < session["number"]:
        session["message"] = "Too low!"
        session["correct"] = False

    elif guess > session["number"]:
        session["message"] = "Too high!"
        session["correct"] = False
    else:
        session["message"] = f"{session['number']} was the number!"
        session["correct"] = True
    return redirect("/")


@app.route("/reset", methods=["POST"])
def reset():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
