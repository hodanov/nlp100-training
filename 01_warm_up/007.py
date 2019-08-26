def gen_sentence(x, y, z):
    sentence = '{}時の{}は{}'.format(x, y, z)
    return sentence


x = 12
y = '気温'
z = 22.4
print(gen_sentence(x, y, z))
