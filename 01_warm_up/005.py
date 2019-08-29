def n_gram(words, n):
    """
    与えられたシーケンス（文字列やリストなど）からn-gramを作成
    """
    n_gram = []
    for i in range(len(words) - n + 1):
        n_gram.append(words[i:i + n])
    return n_gram


words = 'hogehogemogumogu'
for i in range(1, 4):
    print(n_gram(words, i))

words = 'Hello, Python! I like you!'
words = words.split(' ')
for i in range(1, 4):
    print(n_gram(words, i))
