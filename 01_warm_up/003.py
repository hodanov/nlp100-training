import re


def split_words(words: str) -> []:
    """
    単語を分割、リストにして返す。
    """
    words = re.split(' |\\.|\\,', words)
    return words


def count_char(words: []) -> []:
    """
    各単語の（アルファベットの）文字数を先頭から順に並べたリストを作成
    """
    list = []
    for word in words:
        if re.findall('[a-zA-Z]+', word):
            list.append(len(word))
    return list


words = 'Now I need a drink, ' \
        'alcoholic of course, ' \
        'after the heavy lectures involving quantum mechanics.'
print(split_words(words))
print(count_char(split_words(words)))
