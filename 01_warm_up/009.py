import random


def gen_typoglycemia(sentence: str) -> str:
    """
    sentence: str型の引数

    長さが4以下であれば渡された文字列をそのまま返す。
    長さが5以上であれば、最初と最後以外の文字をランダムに並び替える。
    """
    words = sentence.split()
    tmp = []
    for word in words:
        if len(word) >= 5:
            first_letter = word[0]
            last_letter = word[-1]
            random_letter = list(word[1:-1])
            random.shuffle(random_letter)
            word = first_letter + ''.join(random_letter) + last_letter
        tmp.append(word)
    typoglycemia = ' '.join(tmp)
    return typoglycemia


sentence = "I couldn't believe that I could actually understand what " \
    "I was reading : the phenomenal power of the human mind ."
print(sentence)
print(gen_typoglycemia(sentence))
