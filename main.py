import constants
import string

query = input("> ")

query = query.lower()

new_query = ""
for character in query:
    if character not in constants.PUNCTUATION_TO_REMOVE:
        new_query += character

query = new_query

new_query = ""
for word in query.split():
    if word not in constants.STOP_WORDS:
        new_query += word + " "

query = new_query

print(query)