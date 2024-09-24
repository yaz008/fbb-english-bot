from words.const import ANTONYMS, WORDS
from random import choice

def random_pair(exclude_word: str | None = None) -> str:
    word: str = choice(WORDS)
    while word == exclude_word:
        word = choice(WORDS)
    return word, ANTONYMS[word]