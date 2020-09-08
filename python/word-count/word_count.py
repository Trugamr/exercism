import re


def count_words(sentence):
    word_regex = re.compile(r'((?!\')[\w\d]*\'?[\w\d]+)')
    sentence = sentence.replace("_", " ")
    words = {}
    for word in [w.lower() for w in word_regex.findall(sentence)]:
        words.setdefault(word, 0)
        words[word] += 1
    return words
