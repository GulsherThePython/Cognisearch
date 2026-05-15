import constants
from pathlib import Path
import json

notes = Path("notes")
sentence_data_list = []

for file in notes.iterdir():
    with open(file, "r") as f:
        contents = f.read()

        # Split the contents into sentences
        sentences = contents.split(".")

        # Loop through the sentences and process them
        for sentence in sentences:
            sentence_data = {}
            # Normalize the sentence
            og_sentence = sentence
            sentence = sentence.lower()

            new_sentence = ""
            for character in sentence:
                if character not in constants.PUNCTUATION_TO_REMOVE:
                    new_sentence += character
            
            # Remove stop words
            tokens = []
            for word in new_sentence.split():
                if word not in constants.STOP_WORDS:
                    tokens.append(word)

            # Stem the tokens
            for word in range(0, len(tokens)):
                for suffix in constants.SUFFIXES_TO_REMOVE:
                    if tokens[word].endswith(suffix):
                        if len(tokens[word]) > 5:
                            tokens[word] = tokens[word][:-len(suffix)]
                        break
            
            # Extract bigrams
            bigrams = []
            for word in range(0, len(tokens) - 1):
                bigrams.append(tokens[word] + " " + tokens[word + 1])
            
            sentence_data["bigrams"] = bigrams
            sentence_data["tokens"] = tokens
            sentence_data["sentence"] = og_sentence
            sentence_data["source"] = file.name
            sentence_data_list.append(sentence_data)

with open("notes/sentence_data_list.txt", "w") as f:
    json.dump(sentence_data_list, f)