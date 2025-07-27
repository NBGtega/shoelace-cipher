def xor(text, magic_value):
    output = []
    i = 0
    while i < len(text):
        ascii_of_char = ord(text[i])
        acii_of_mvalue = ord(magic_value[i % len(magic_value)])     #the index is always within bounds of length of magic magic_value
        encrypted = chr(ascii_of_char ^ acii_of_mvalue)
        output.append(encrypted)
    return ''.join(output)

def reverse(text):
    text_list = list(text)
    text_list.reverse()
    return ''.join(text_list)

def check(expected_lower, actual_lower, expected_upper, actual_upper):
    if actual_upper == expected_upper:
        print("Passed uppercase test")
    else:
        print("Failed uppercase test")
        cause(expected_upper, actual_upper)

    if actual_lower == expected_lower:
        print("Passed lowercase")
    else:
        print("Failed lowercase test")
        cause(expected_lower, actual_lower)


def cause(expected, actual):
    i = 0
    expected_list = []
    errored_list = []

    while i < len(expected):
        if expected[i] != actual[i]:
            expected_list.append(expected[i])
            errored_list.append(actual[i])
        i += 1

    i = 0
    print("Bug(s) found!")        
    while i < len(expected_list):
        print(f"Expected: {expected_list[i]}        Actual: {errored_list[i]}")
        i += 1




