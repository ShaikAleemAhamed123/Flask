from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


@app.route("/")
def template():
    return render_template("template.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
