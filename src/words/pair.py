from words.const import ANTONYMS, WORDS
from random import choice

def random_pair() -> str:
    word: str = choice(WORDS)
    return f'{word}: ||{ANTONYMS[word]}||'