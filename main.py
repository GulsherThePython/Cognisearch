import constants
import os

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
            if len(tokens[word]) > 5:
                tokens[word] = tokens[word][:-len(suffix)]
            break

# Extract bigrams

bigrams = []
for word in range(0, len(tokens) - 1):
    bigrams.append(tokens[word] + " " + tokens[word + 1])

print(bigrams)