import constants
from tools import is_fuzzy_match
from sentence import Sentence
from proccess_notes import main as proccess_notes
import os
import json

# Ask user if they want to proccess the notes

q = input("Would you like to proccess the notes? (y/n) > ")
if q == "y":
    proccess_notes()

# Get the query from the user
inp = input("Enter the query > ")
query = inp

# Process query

query = Sentence(query, "query")
query.process_sentence()

# Begin searching through the notes

sentence_data_list = []
with open(os.path.join("notes", "sentence_data_list.txt"), "r") as f:
    sentence_data_list = json.loads(f.read())

scores = []
for sentence in sentence_data_list:
    score = 0
    for token in query.tokens:
        for s_token in sentence["tokens"]:
            if constants.is_fuzzy_match(token, s_token):
                score += 1
                break
    
    for bigram in query.bigrams:
        for s_bigram in sentence["bigrams"]:
            if constants.is_fuzzy_match(bigram, s_bigram):
                score += 2
                break
    
    scores.append({sentence: score})

def get_score(item):
    return list(item.values())[0]
scores.sort(key=get_score, reverse=True)

print(scores[0])