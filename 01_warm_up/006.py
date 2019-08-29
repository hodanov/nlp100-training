"""
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，
それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ
"""


def n_gram(words, n):
    n_gram = []
    for i in range(len(words) - n + 1):
        n_gram.append(words[i:i + n])
    return n_gram


word1 = 'paraparaparadise'
word2 = 'paragraph'

x = n_gram(word1, 2)
y = n_gram(word2, 2)
print('---bi_gram---')
print(x)
print(y)

x = set(x)
y = set(y)
print('---set---')
print(x)
print(y)

and_set = x.union(y)
print('---And set---')
print(and_set)

product_set = x.intersection(y)
print('---Product set---')
print(product_set)

difference_set = x.difference(y)
print('---Difference set---')
print(difference_set)

print('---Is "se" included?---')
print('Is "se" included x?')
print('se' in x)

print('Is "se" included y?')
print('se' in y)
