def frequency_sort(items):
    items_freq = dict()
    answer = list()

    for item in items:
        item_exist = items_freq.get(item, None)
        if item_exist:
            items_freq.update({item: item_exist + 1})
        else:
            items_freq.update({item: 1})
    sorted_values = dict(sorted(items_freq.items(), key=lambda item: item[1], reverse=True))
    for key, value in sorted_values.items():
        answer.extend([key] * value)
    return answer


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
