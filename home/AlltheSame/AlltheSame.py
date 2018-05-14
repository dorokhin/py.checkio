from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    return len(set(elements)) < 2


def all_the_same2(data):
    return all(x == y for x, y in zip(data, data[1:]))


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same2(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
