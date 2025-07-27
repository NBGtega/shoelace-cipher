def xor(text, magic_value):
    output = []
    i = 0
    while i < len(text):
        ascii_of_char = ord(text[i])
        acii_of_mvalue = ord(magic_value[i % len(magic_value)])     #the index is always within bounds of length of magic magic_value
        encrypted = chr(ascii_of_char ^ acii_of_mvalue)
        output.append(encrypted)
        i += 1
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

def y_and_z_check(current_val, y_ascii, Y_ascii, z_ascii, Z_ascii, output):
    if current_val == y_ascii:
        output.append(chr(ord('a')))
    elif current_val ==  Y_ascii:
        output.append(chr(ord('A')))
    elif current_val ==  z_ascii:
        output.append(chr(ord('b')))
    elif current_val == Z_ascii:
        output.append(chr(ord('B')))
    return output

def b_x_and_y_check(current_val, B_ascii, b_ascii, X_ascii, x_ascii, Y_ascii, y_ascii, output):
    if current_val == B_ascii:
        output.append(chr(ord('C')))
    elif current_val ==  b_ascii:
        output.append(chr(ord('c')))
    elif current_val ==  X_ascii:
        output.append(chr(ord('A')))
    elif current_val == x_ascii:
        output.append(chr(ord('a')))
    elif current_val ==  Y_ascii:
        output.append(chr(ord('D')))
    elif current_val == y_ascii:
        output.append(chr(ord('d')))
    return output


