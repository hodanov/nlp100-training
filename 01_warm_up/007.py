def gen_sentence(x, y, z):
    """
    引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装
    """
    sentence = '{}時の{}は{}'.format(x, y, z)
    return sentence


x = 12
y = '気温'
z = 22.4
print(gen_sentence(x, y, z))
