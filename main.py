import constants
import os
import json
import proccess_notes

# Ask user if they want to proccess the notes

inp = input("Would you like to proccess the notes? (y/n) > ")
if inp == "y":
    proccess_notes.main()

# Get the query from the user
inp = input("Enter the query > ")
query = inp

# Normalize the query
query = query.lower()

new_query = ""
for character in query:
    if character not in constants.PUNCTUATION_TO_REMOVE:
        new_query += character

# Remove stop words

tokens = []
for word in new_query.split():
    if word not in constants.STOP_WORDS:
        tokens.append(word)

# Stem the tokens

for word in range(0, len(tokens)):
    for suffix in constants.SUFFIXES_TO_REMOVE:
        if tokens[word].endswith(suffix):
            if len(tokens[word]) >= 5:
                tokens[word] = tokens[word][:-len(suffix)]
            break

# Extract bigrams

bigrams = []
for word in range(0, len(tokens) - 1):
    bigrams.append(tokens[word] + " " + tokens[word + 1])

# Begin searching through the notes

# Example sentences
sentence_data_list = []
with open(os.path.join("notes", "sentence_data_list.txt"), "r") as f:
    sentence_data_list = json.loads(f.read())

scores = []
for sentence in sentence_data_list:
    score = 0
    for token in tokens:
        if token in sentence["tokens"]:
            score += 1
    
    scores.append({sentence["sentence"]: score})

def get_score(item):
    return list(item.values())[0]

scores.sort(key=get_score, reverse=True)

print(scores[0])