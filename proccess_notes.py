from sentence import Sentence
from pathlib import Path
import json
import os

def main():
    with open(os.path.join("notes", "sentence_data_list.txt"), "w") as f:
        f.write("")
    notes = Path("notes")
    sentence_data_list = []

    for file in notes.iterdir():
        with open(file, "r") as f:
            contents = f.read()

            sentences = contents.split(".")
            for sentence in sentences:
                sentence_data = Sentence(sentence, file.stem)
                sentence_data.process_sentence()
                sentence_data_list.append({
                    "sentence": sentence_data.sentence,
                    "tokens": sentence_data.tokens,
                    "bigrams": sentence_data.bigrams,
                    "source": sentence_data.source
                })

    with open(os.path.join("notes", "sentence_data_list.txt"), "w") as f:
        json.dump(sentence_data_list, f)