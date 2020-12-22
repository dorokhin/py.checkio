sum_numbers = lambda text: sum(int(word) for word in text.split() if word.isdigit())


def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def sum_numbers2(text: str) -> int:
    result = 0
    cleared = [x for x in text.split(' ') if is_int(x)]
    for item in cleared:
        result += int(item)
    return result


if __name__ == '__main__':
    print("Example:")
    print(sum_numbers('hi'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_numbers('hi') == 0
    assert sum_numbers('who is 1st here') == 0
    assert sum_numbers('my numbers is 2') == 2
    assert sum_numbers('This picture is an oil on canvas '
                       'painting by Danish artist Anna '
                       'Petersen between 1845 and 1910 year') == 3755
    assert sum_numbers('5 plus 6 is') == 11
    assert sum_numbers('') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
