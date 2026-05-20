from flask import Flask, redirect, url_for, render_template, request
from engine import run
from pathlib import Path
from proccess_notes import main as process_notes

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

@app.route("/notes")
def notes():
    notes_path = Path("notes")
    notes_list = []
    for file in notes_path.iterdir():
        if file.stem == "sentence_data_list":
            continue
        with open(file, "r") as f:
            raw_contents = f.read().split("\n\n")
            contents = []
            for note in raw_contents:
                if note.strip() != "":
                    contents.append(note)
            notes_list.append(contents)
    
    actual_notes_list = []
    for note in notes_list:
        for line in note:
            actual_notes_list.append(line)
        
    return render_template("notes.html", notes=actual_notes_list)

@app.route("/add_note", methods=["POST"])
def add_note():
    note = request.form["note"]
    with open("notes/user_notes.txt", "a") as f:
        f.write(note.strip() + "\n\n")
    
    process_notes()
    return redirect(url_for("notes"))

@app.route("/delete_note/<int:note_index>")
def delete_note(note_index):
    notes_path = Path("notes")

    # Build list of (note, file)
    all_notes = []
    for file in notes_path.iterdir():
        if file.stem == "sentence_data_list":
            continue

        with open(file, "r") as f:
            raw_contents = f.read().split("\n\n")

            for note in raw_contents:
                if note.strip():
                    all_notes.append([note, file])

    # Safety check
    if note_index < 0 or note_index >= len(all_notes):
        return redirect(url_for("notes"))

    # Find target
    target_note = all_notes[note_index][0]
    target_file = all_notes[note_index][1]

    # Delete the target note from the file
    with open(target_file, "r") as f:
        raw_contents = f.read().split("\n\n")

    updated_notes = [note for note in raw_contents if note.strip() and note != target_note]

    # Rewrite the file with the updated notes
    with open(target_file, "w") as f:
        f.write("\n\n".join(updated_notes))

    process_notes()

    return redirect(url_for("notes"))