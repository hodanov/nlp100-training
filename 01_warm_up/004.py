import re


def get_element_symbols(words):
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
