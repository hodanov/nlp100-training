import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def merge_two_words(x: str, y: str):
    """
    与えられた2つの文字列を交互に結合する。
    """
    merged_word = ''
    for i in range(4):
        merged_word += x[i]
        merged_word += y[i]
    return merged_word


word1 = 'パトカー'
word2 = 'タクシー'
print(merge_two_words(word1, word2))
