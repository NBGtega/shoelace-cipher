#these two xor functions made by gpt bcz I'm not crazy enough to fry my brain cells
def xor_encrypt_hex(text, magic_value):
    magic_value = magic_value * (len(text) // len(magic_value) + 1)
    encrypted = ''.join(f"{ord(c) ^ ord(k):02x}" for c, k in zip(text, magic_value))
    return encrypted

def xor_decrypt_hex(hex_string, magic_value):
    encrypted = bytes.fromhex(hex_string)
    magic_value = magic_value * (len(encrypted) // len(magic_value) + 1)
    return ''.join(chr(b ^ ord(k)) for b, k in zip(encrypted, magic_value))

#print(xor_decrypt_hex(xor_encrypt_hex("Fuck you", "kaboom"), "kaboom"))

def hex_for_str(text):
    output = []
    i = 0
    while i < len(text):
        ascii_value = ord(text[i])
        hex_value = hex(ascii_value)[2:]    #remove first 0x from hex before appending
        output.append(hex_value)
        i += 1
    return "".join(output)

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

def y_and_z_check(current_val, y_ascii, Y_ascii, z_ascii, Z_ascii):
    ascii_val = 0
    if current_val == y_ascii:
        ascii_val = ord('a')
    elif current_val ==  Y_ascii:
        ascii_val = ord('A')
    elif current_val ==  z_ascii:
        ascii_val = ord('b')
    elif current_val == Z_ascii:
        ascii_val = ord('B')
    return ascii_val

