def xor(text, magic_value):             #converts text, magic_value to ascii, does xor between them, converts back to char, returns
    output = []
    i = 0
    while i < len(text):
        ascii_of_char = ord(text[i])
        acii_of_mvalue = ord(magic_value[i % len(magic_value)])     #the index is always within bounds of length of magic magic_value
        encrypted = chr(ascii_of_char ^ acii_of_mvalue)
        output.append(encrypted)
        i += 1
    return ''.join(output)

def reverse(text):  #as the name suggests, reverses and returns string
    text_list = list(text)
    text_list.reverse()
    return ''.join(text_list)

def check(expected_lower, actual_lower, expected_upper, actual_upper):      #checker function to find bugs while development
    if actual_upper == expected_upper:
        print("Passed uppercase test")
    else:
        print("Failed uppercase test")
        cause(expected_upper, actual_upper)

    if actual_lower == expected_lower:
        print("Passed lowercase test")
    else:
        print("Failed lowercase test")
        cause(expected_lower, actual_lower)


def cause(expected, actual):        #finds causes of bugs
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
#print(xor(xor("ABCDEF", "kaboom"), "kaboom"))
