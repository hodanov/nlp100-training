import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def getOddChar(word: str):
    """
    文字列の奇数番目の文字を取り出して連結する。
    """
    return word[::2]


word = 'パタトクカシー'
print(getOddChar(word))
