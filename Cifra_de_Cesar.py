alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 0123456789.,:;!?()"
length = len(alphabet)


def cipher_word(word: str, key: int) -> str:
    code = ''
    for char in word:
        code += next_char(char, key)
    return code


def next_char(char: str, key: int) -> str:
    index = alphabet.index(char)
    if index + key >= length:
        value = index + key - length - 1
        return alphabet[0 + value]
    return alphabet[index + key]


def decipher_word(word: str, key: int) -> str:
    code = ''
    for char in word:
        code += previous_char(char, key)
    return code


def previous_char(char: str, key: int) -> str:
    index = alphabet.index(char)
    if index - key <= 0:
        value = length + (index - key)
        return alphabet[value]
    return alphabet[index - key]


def brute_force(word: str) -> str:
    path = "\\dicionário"
    file = open(path)
    

    file.close()

