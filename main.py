import constants
import string

inp = input("> ")

query = inp

query = query.lower()

new_query = ""
for character in query:
    if character not in constants.PUNCTUATION_TO_REMOVE:
        new_query += character


tokens = []
for word in new_query.split():
    if word not in constants.STOP_WORDS:
        tokens.append(word)

bigrams = []
for word in range(0, len(tokens) - 1):
    bigrams.append(tokens[word] + " " + tokens[word + 1])

print(bigrams)