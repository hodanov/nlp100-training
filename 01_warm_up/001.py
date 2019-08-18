import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def getOddChar(word):
    i = 0
    odd_chars = ''
    for char in word:
        i += 1
        if i % 2 == 1:
            odd_chars += char
    return odd_chars


word = 'パタトクカシー'
print(getOddChar(word))
