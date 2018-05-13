def checkio(words: str) -> bool:
    word_count = 0
    for word in words.split():
        if word.isalpha():
            word_count += 1
        else:
            word_count = 0
        if word_count == 3:
            return True

    return False


checkio2 = lambda words: True if "True, True, True" in "".join(str([x.isalpha() for x in words.split()])) else False


def checkio3(s):
    l = [x.isalpha() for x in s.split()]
    return [True]*3 in [l[i:i+3] for i in range(len(l)-2)]


if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
