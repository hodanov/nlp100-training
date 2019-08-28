def cipher(chars: str) -> str:
    """
    chars: str型の引数
    result: str型の返り値

    文字がa~zの範囲内（小文字の英語）の時、文字を変換。
    a~z以外の場合はそのまま変数resultへ格納する。

    def hogehoge(x: type) -> type:
    ↑これはver3.5から導入された型アノテーション（https://www.python.org/dev/peps/pep-0484/）
    """
    result = ''
    for c in chars:
        if 'a' <= c <= 'z':
            result += chr(219 - ord(c))
        else:
            result += c
    return result


chars = 'She is a super saiyan!!'
print('---Input chars ---')
print(chars)

print('---Cipher chars ---')
print(cipher(chars))

print('---ReCipher chars ---')
print(cipher(cipher(chars)))
