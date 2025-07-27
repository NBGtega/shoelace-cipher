from helper_func import y_and_z_check, b_x_and_y_check

y_ascii = ord('y')
Y_ascii = ord('Y')
z_ascii = ord('z')
Z_ascii = ord('Z')


def crisscross(text):

    i = 0                                   #itereator
    list_of_char = list(text)               #list of input text
    output = []                             #output var

    while i < len(text):                    #runs till all characters are converted
        ascii_value = ord(list_of_char[i])  #ascii value of letter
        if ascii_value in range(ord('A'), Y_ascii) or ascii_value in range(ord('a'), y_ascii):    #check if the char is within A-X or a-x character limit

            if ascii_value % 2 == 0:            #check if it's even
                ascii_value += 1                #step of one char forward
            else:
                ascii_value += 3                #step of 3 char forward

        elif ascii_value in [y_ascii, Y_ascii, z_ascii, Z_ascii]:   #check if its y or z and handle those cases
            if ascii_value == y_ascii:
                output.append(chr(ord('b')))
            elif ascii_value ==  Y_ascii:
                output.append(chr(ord('B')))
            elif ascii_value ==  z_ascii:
                output.append(chr(ord('a')))
            elif ascii_value == Z_ascii:
                output.append(chr(ord('A')))
            i += 1
            continue

        else:
            raise ValueError(f'Error: "{chr(ascii_value)}" is not supported \nOnly letters are supported')
        
        output.append(chr(ascii_value))     #appending after converting back to chr
        i += 1

    return output

def army(text):
    i = 0                                                                       
    output = []                             

    while i < len(text):            #runs till all characters are converted
        ascii_value = ord(text[i])  #ascii value of letter
        if ascii_value in range(ord('A'), Y_ascii) or ascii_value in range(ord('a'), y_ascii): #check if the char is within A-Z character limit
            #Here I am checking if the direction towards the next letter is downwards or diagonal
            #If % 2 == 0, it could mean 2 steps ahead or 3.
            if ascii_value % 4 == 0: 
                ascii_value +=1
            else:
                if ascii_value % 2 != 0 and (ascii_value + 1) % 4 == 0:
                    ascii_value +=3
                else:
                    ascii_value +=2
            output.append(chr(ascii_value))     #appending after converting back to chr
        elif ascii_value in [y_ascii, Y_ascii, z_ascii, Z_ascii]:
            output = y_and_z_check(ascii_value, y_ascii, Y_ascii, z_ascii, Z_ascii, output)
            
        else:
            raise ValueError(f'Error: "{chr(ascii_value)}" is not supported \nOnly letters are supported')
        i += 1

    return output
            
def straight_european(text):
    i = 0                                                                       
    output = []
    ascii_vals = [x for x in range(ord('A'), ord('Z') + 1) if x != ord('B') and x != ord('X') and x != ord('Y')]
    lower_ascii = [x for x in range(ord('a'), ord('z') + 1) if x != ord('b') and x != ord('x') and x != ord('y')]
    ascii_vals.extend(lower_ascii)

    while i < len(text):            #runs till all characters are converted
        ascii_value = ord(text[i])  #ascii value of letter
        if ascii_value in ascii_vals:
           if ascii_value % 4 == 0:
               ascii_value +=3
           elif ascii_value % 4 == 1:
               ascii_value +=5
           elif ascii_value % 4 == 2:
               ascii_value -=1
           elif ascii_value % 4 == 3:
               ascii_value +=1
           output.append(chr(ascii_value))
        elif ascii_value in [ord('B'), ord('X'), ord('b'), ord('x'), Y_ascii, y_ascii]:
           output = b_x_and_y_check(ascii_value, ord('B'), ord('b'), ord('X'), ord('x'), Y_ascii, y_ascii, output)
        
        else:
            raise ValueError(f'Error: "{chr(ascii_value)}" is not supported \nOnly letters are supported')
        i += 1
    
    return output