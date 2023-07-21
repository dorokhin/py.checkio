from collections.abc import Iterable


def duplicate_zeros(donuts: list[int]) -> Iterable[int]:
    result = list()
    [result.extend([0, 0]) if x == 0 else result.append(x) for x in donuts]
    return result


if __name__ == '__main__':
    assert list(duplicate_zeros([0, 0, 0, 0])) == [0, 0, 0, 0, 0, 0, 0, 0]
    assert list(duplicate_zeros([100, 10, 0, 101, 1000])) == [100, 10, 0, 0, 101, 1000]
