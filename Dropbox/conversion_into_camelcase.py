def to_camel_case(name):

    return ''.join(x.title() for x in name.split('_'))


if __name__ == '__main__':
    print("Example:")
    print(to_camel_case('name'))

    assert to_camel_case("my_function_name") == "MyFunctionName"
    assert to_camel_case("i_phone") == "IPhone"
    assert to_camel_case("this_function_is_empty") == "ThisFunctionIsEmpty"
    assert to_camel_case("name") == "Name"
    print("Coding complete? Click 'Check' to earn cool rewards!")
