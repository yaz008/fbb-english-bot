from json import load

with open(file='assets\\antonyms.json', mode='r', encoding='UTF-8') as antonyms_file:
    ANTONYMS: dict[str, str] = load(antonyms_file)
    WORDS: list[str] = list(ANTONYMS.keys())