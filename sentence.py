from constants import PUNCTUATION_TO_REMOVE, STOP_WORDS, SUFFIXES_TO_REMOVE

class Sentence:
    def __init__(self, sentence, source):
        self.sentence = sentence
        self.source = source
        self.tokens = []
        self.bigrams = []
    
    def process_sentence(self):
        # Normalize the sentence
        sentence = self.sentence.lower()

        new_sentence = ""
        for character in sentence:
            if character not in PUNCTUATION_TO_REMOVE:
                new_sentence += character
        
        # Remove stop words
        tokens = []
        for word in new_sentence.split():
            if word not in STOP_WORDS:
                tokens.append(word)

        # Stem the tokens
        for word in range(0, len(tokens)):
            for suffix in SUFFIXES_TO_REMOVE:
                if tokens[word].endswith(suffix):
                    if len(tokens[word]) > 5:
                        tokens[word] = tokens[word][:-len(suffix)]
                    break
        
        # Extract bigrams
        bigrams = []
        for word in range(0, len(tokens) - 1):
            bigrams.append(tokens[word] + " " + tokens[word + 1])
        
        self.tokens = tokens
        self.bigrams = bigrams

