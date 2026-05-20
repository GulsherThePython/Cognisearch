from flask import Flask, redirect, url_for, render_template, request
from engine import run

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["POST", "GET"])
def search():
    if request.method == "POST":
        query = request.form["query"]
        raw_results = run(query)[0:5]
        results = []
        for result in raw_results:
            if result[1] != 0:
                results.append(result)
        return render_template("results.html", results=results, query=query, count=len(results))
    return render_template("search.html")

@app.route("/about")
def about():
    return render_template("about.html")
