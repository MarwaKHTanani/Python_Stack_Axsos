from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    x = 8
    y = 8
    return render_template("index.html", x=x, y=y)


@app.route("/4")
def eight_by_four():
    x = 8
    y = 4
    return render_template("index.html", x=x, y=y)


@app.route("/<int:x>/<int:y>")
def x_by_y(x, y):
    return render_template("index.html", x=x, y=y)


if __name__ == "__main__":
    app.run(debug=True)
