def collatz_convert(data: int | str) -> int | str | None:
    """
    https://py.checkio.org/en/mission/collatz-ztalloc/share/bfc19e14bd5954cb21e6655ae7e2e996/

    The Collatz conjecture is one of the most famous unsolved problems in mathematics.
    However, the Collatz sequence can also be viewed in a binary fashion depending
    on whether each value steps up (3x+1) or down (x/2) from the previous value,
    denoting these steps with "u", "d", respectively.
    """
    buffer = ''
    if isinstance(data, str):
        initial = 1
        prev = ''
        for i in data[::-1]:
            if (initial < 1) or (i == prev):
                return None
            if i == 'd':
                initial *= 2
                prev = ''
            else:
                initial = (initial - 1) / 3
                prev = i
        print(type(initial))
        return initial
    elif isinstance(data, int):
        while data != 1:
            if data % 2 == 0:
                data = data / 2
                buffer += 'd'
            else:
                data = data * 3 + 1
                buffer += 'u'
        return buffer



print("Example:")
# print(collatz_convert(15))

# These "asserts" are used for self-checking
assert collatz_convert("ududududddddudddd") == 15
assert collatz_convert(135) == "udududduddddududdudduddddudududdudddudddd"
assert collatz_convert("dudududdudddudddd") == 14
assert collatz_convert(10) == "dudddd"

print("The mission is done! Click 'Check Solution' to earn rewards!")
