# Important lists of constants used throughout the codebase

PUNCTUATION_TO_REMOVE = [
    ".", ",", "?", "!", ";", ":", "'", '"',
    "(", ")", "[", "]", "{", "}",
    "-", "—", "-",
    "...", "…",
    "/", "\\",
    "@", "#", "$", "%", "&", "*",
    "+", "=", "<", ">", "|",
    "~", "`",
]

STOP_WORDS = [
    "a", "an", "the",

    "at", "be", "by", "for", "from",
    "has", "have", "had",
    "having",

    "he", "she", "it", "its", "they", "we", "you", "i",
    "him", "her", "them", "us",
    "me", "my", "mine", "your", "yours", "our", "ours",

    "in", "on", "of", "to", "with", "into", "onto", "over", "under",
    "about", "between", "through", "during", "before", "after",

    "is", "are", "was", "were", "been", "am", "being",

    "will", "would", "can", "could", "shall", "should", "may", "might", "must",

    "do", "does", "did", "doing",

    "and", "or", "but", "yet", "so",

    "not", "no", "nor",

    "if", "then", "else", "when", "while", "where", "why", "how",

    "as", "than",

    "this", "that", "these", "those",

    "there", "here",

    "what", "which", "who", "whom"
]

SUFFIXES_TO_REMOVE = [
    "tion", "ment", "less", "ness", "ning", "ing", "ful", "ed", "ly", "es", "s",
]

# Importand Functions used throughout the codebase

# Fuzzy matching for string similarity
def is_fuzzy_match(a, b):
    # If they are identical, they are a match
    if a == b:
        return True

    # If the lengths are too different, they are not a match
    if abs(len(a) - len(b)) > 2:
        return False

    # check character overlap
    common = 0
    for char in a:
        if char in b:
            common += 1
    
    # Compute the fraction of characters that overlap to the length of the longer word
    char_overlap_similarity = common / (len(a) if len(a) > len(b) else len(b))

    return char_overlap_similarity > 0.7

    # TODO: Implement Bigram fuzzy matching as well

# Important classes

# Sentence Class
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

