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