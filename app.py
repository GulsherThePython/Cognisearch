from flask import Flask, redirect, url_for, render_template, request
from engine import run

app = Flask(__name__)

@app.route("/")
def home():
    return redirect( url_for("search") )

@app.route("/search", methods=["POST", "GET"])
def search():
    if request.method == "POST":
        return render_template("results.html", results=run(request.form["query"])[0:5])
    return render_template("search.html")


