def number_length(value: int) -> int:
    digits = 1
    while value >= 10:
        value = value / 10
        digits += 1
    return digits


print("Example:")
print(number_length(10))
# These "asserts" are used for self-checking
assert number_length(10) == 2
assert number_length(0) == 1
assert number_length(4) == 1
assert number_length(44) == 2