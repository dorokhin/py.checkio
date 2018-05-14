def checkio(d: str) -> bool:
    return True if len(d) >= 10 and any(c.isdigit() for c in d) and any(c.isupper() for c in d) and any(c.islower() for c in d)else False


if __name__ == '__main__':
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
