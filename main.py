import constants
import string

inp = input("> ")

query = inp

query = query.lower()

new_query = ""
for character in query:
    if character not in constants.PUNCTUATION_TO_REMOVE:
        new_query += character


query_words = []
for word in new_query.split():
    if word not in constants.STOP_WORDS:
        query_words.append(word)

query = ""
for word in query_words:
    query += word + " "

query = query.strip()

print(query)