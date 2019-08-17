import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def join(x, y):
    joined_word = ''
    i = 0
    for i in range(4):
        joined_word += x[i]
        joined_word += y[i]
        i += 1
        print(i)
    return joined_word


word1 = 'パトカー'
word2 = 'タクシー'
print(join(word1, word2))
