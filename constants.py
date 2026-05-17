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
