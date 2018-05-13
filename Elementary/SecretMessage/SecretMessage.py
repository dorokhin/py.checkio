def find_message(text: str) -> str:
    return ''.join(x * x.isupper() for x in text)


def find_message2(text: str) -> str:
    return ''.join(filter(str.isupper, text))


if __name__ == '__main__':

    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
