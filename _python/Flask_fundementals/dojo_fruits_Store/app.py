from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/checkout", methods=["POST"])
def checkout():
    strawberry = int(request.form["strawberry"])
    apple = int(request.form["apple"])
    raspberry = int(request.form["raspberry"])
    name = request.form["name"]
    id = request.form["id"]
    count=strawberry+raspberry+apple
    return render_template(
        "info.html",
        strawberry=strawberry,
        apple=apple,
        raspberry=raspberry,
        name=name,
        id=id,
        count=count
    )


if __name__ == "__main__":
    app.run(debug=True)
