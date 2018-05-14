def safe_pawns(pawns: set) -> int:
    pawns_indexes = set()
    for p in pawns:
        row = int(p[1]) - 1
        col = ord(p[0]) - 97
        pawns_indexes.add((row, col))

    count = 0
    for row, col in pawns_indexes:
        is_safe = ((row - 1, col - 1) in pawns_indexes) or ((row - 1, col + 1) in pawns_indexes)
        if is_safe:
            count += 1
    return count


def safe_pawns2(pawns):
    f = lambda x: (chr(ord(x[0])-1) + str(int(x[-1])-1), chr(ord(x[0])+1) + str(int(x[-1])-1))
    return len([x for x in pawns if f(x)[0] in pawns or f(x)[-1] in pawns])


if __name__ == '__main__':
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
