def checkio(expression):
    valid_items = ('{', '}', '(', ')', '[', ']')
    open_items = ('{', '(', '[')

    item_pairs = {'}': '{', ')': '(', ']': '['}
    stack = list()
    cleared_string = [x for x in expression if x in valid_items]
    print(cleared_string)
    for item in cleared_string:
        if len(stack) == 0 and item not in open_items:
            return False
        if item in open_items:
            stack.append(item)
        else:
            if item_pairs[item] != stack.pop():
                return False
    if len(stack) != 0:
        return False
    return True


def checkio2(expression):
    brackets = {'{': '}', '[': ']', '(': ')'}
    stack = []
    for a in expression:
        if a in brackets.keys():
            stack.append(brackets[a])
        elif a in brackets.values():
            if not stack: return False
            elif stack.pop() != a: return False
    return not stack


if __name__ == "__main__":
    print(checkio("((5+3)*2+1)") == True)
    print(checkio("{[(3+1)+2]+}") == True)
    print(checkio("(3+{1-1)}") == False)
    print(checkio("[1+1]+(2*2)-{3/3}") == True)
    print(checkio("(({[(((1)-2)+3)-3]/3}-3)") == False)
    print(checkio("2+3") == True)
