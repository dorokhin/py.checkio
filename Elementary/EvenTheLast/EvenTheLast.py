def checkio(array_):
    return 0 if len(array_) == 0 else sum(array_[::2]) * array_[-1]


def checkio2(array_):
    return sum(array_[::2])*array_[-1] if array_ else 0


if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
