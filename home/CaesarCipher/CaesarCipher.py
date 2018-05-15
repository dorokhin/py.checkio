def shift_char(char, delta):
    base_ord = ord('a')
    return chr(base_ord + (ord(char) - base_ord + delta) % 26)


def to_encrypt(text, delta):
    char_list = [shift_char(i, delta) if 'a' <= i <= 'z' else i for i in text]
    return ''.join(char_list)


def to_encrypt2(text, delta):
    f = lambda c: chr((ord(c) + 7 + delta) % 26 + 97) if c.isalpha() else c
    return ''.join(map(f, text))


if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', 10))
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
