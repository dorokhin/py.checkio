def checkio(number: int) -> int:
    number = str(number)
    result = 1
    for num in number:
        if int(num) != 0:
            result *= int(num)
    return result


def checkio2(number):
    return eval('*'.join(i for i in str(number) if i != '0'))


def checkio3(number):
    return (lambda f: f([int(n) for n in (str(number)) if n > "0"],
                        f))(lambda list_, f: f(list_[1:], f) * list_[0] if len(list_) > 1 else list_[0])


if __name__ == '__main__':
    assert checkio3(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
