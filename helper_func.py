def xor(text, magic_value):
    output = []
    i = 0
    while i < len(text):
        ascii_of_char = ord(text[i])
        acii_of_mvalue = ord(magic_value[i % len(magic_value)])     #the index is always within bounds of length of magic magic_value
        encrypted = chr(ascii_of_char ^ acii_of_mvalue)
        output.append(encrypted)
    return ''.join(output)
