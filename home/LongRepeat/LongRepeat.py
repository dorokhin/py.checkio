def long_repeat(line):
    return max([i for i in range(1, len(line) + 1)
                if any([True for char in line if line.find(char * i) != -1])]) if line != '' else 0


def long_repeat2(line):
    return len(line) and 1+long_repeat(''.join(u for u,v in zip(line,line[1:]) if u==v))


long_repeat3 = lambda l: len(l)and max(map(len, dict(__import__('re').findall(r'((.)\2*)', l))))


if __name__ == '__main__':
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
