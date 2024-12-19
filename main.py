import deepcut
from words.common_words import common_words
import re

def translate(words):
    result = deepcut.tokenize(words)
    res = ""

    for word in result:
        if word in common_words:
            res = res + common_words[word]
        elif re.match(r'[\u0E00-\u0E7F]*า[\u0E01-\u0E2E\u0E2F\u0E3A]+', word):
            res = res + word + "ฯ"
        elif re.search(r'[\u0E00-\u0E7F]*า[\u0E01-\u0E2E\u0E2F\u0E3A]+', word):
            a = word.replace('ว', 'วฯ')
            b = re.sub(r'([ก-ฮ])$', r'\1ๆ', word)
            res = res + b
        else:
            res = res + word
        
    return res

if __name__ == "__main__":
    word = input("Input thai word: ")
    print(translate(word))