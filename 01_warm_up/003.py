import re


def split_words(words):
    words = re.split(' |\\.', words)
    return words


words = 'Now I need a drink,' \
        'alcoholic of course,' \
        'after the heavy lectures involving quantum mechanics.'
print(split_words(words))
