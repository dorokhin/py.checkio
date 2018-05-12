def checkio(num_: int) -> str:
    return "Fizz Buzz" if num_ % 15 == 0 else 'Fizz' if num_ % 3 == 0 else 'Buzz' if num_ % 5 == 0 else str(num_)


if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"

