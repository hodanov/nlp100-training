import re


def get_element_symbols(words: str) -> {}:
    """
    文章を単語に分解，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
    それ以外の単語は先頭の2文字を取り出す。
    取り出した文字列から単語の位置（先頭から何番目の単語か）への
    連想配列（辞書型もしくはマップ型）を返す。
    """
    element_symbols = {}
    i = 1
    words = re.split(' |\\. |\\.', words)
    for word in words:
        if i in (1, 5, 6, 7, 8, 9, 15, 16, 19):
            element_symbols.update({i: word[0:1]})
        else:
            element_symbols.update({i: word[0:2]})
        i += 1
    return element_symbols


words = 'Hi He Lied Because Boron Could Not Oxidize Fluorine.' \
        'New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
print(get_element_symbols(words))
