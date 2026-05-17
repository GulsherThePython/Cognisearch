import constants
import os
import json

inp = input("> ")
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
sentence_data_list = [
    {
        "sentence": "Hello world, my name is Gulsher the Python", 
        "tokens": ["hello", "world", "name", "gulsher", "python"],
        "bigrams": ["hello world", "world name", "name gulsher", "gulsher python"],
        "source": "test.txt"
    },
    {
        "sentence": "I am learning make names in Python", 
        "tokens": ["learning", "make", "names", "python"],
        "bigrams": ["learning make", "make names", "names python"],
        "source": "test.txt"
    },
    {
        "sentence": "Python is a great programming language that Gulsher loves naming", 
        "tokens": ["python", "great", "programming", "language", "gulsher", "loves", "naming"],
        "bigrams": ["python great", "great programming", "programming language", "language gulsher", "gulsher loves", "loves naming"],
        "source": "test.txt"
    }
]
# with open(os.path.join("notes", "sentence_data_list.txt"), "r") as f:
#     sentence_data_list = json.load(f)

scores = []
for sentence in sentence_data_list:
    score = 0
    for token in tokens:
        if token in sentence["tokens"]:
            score += 1
    
    scores.append({sentence["sentence"]: score})

print(scores)