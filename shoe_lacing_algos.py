from helper_func import y_and_z_check

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
        if ascii_value in range(ord('A'), Y_ascii) or ascii_value in range(ord('a'), y_ascii) or ascii_value == ord(" "):    #check if the char is within A-X or a-x character limit

            if ascii_value % 2 == 0:            #check if it's even
                ascii_value += 1                #step of one char forward
            else:
                ascii_value += 3                #step of 3 char forward

        elif ascii_value in [y_ascii, Y_ascii, z_ascii, Z_ascii]:   #special cases, no pattern
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

    return ''.join(output)

def army(text):
    i = 0                                                                       
    output = []                             

    while i < len(text):            #runs till all characters are converted
        ascii_value = ord(text[i])  #ascii value of letter
        if ascii_value in range(ord('A'), Y_ascii) or ascii_value in range(ord('a'), y_ascii) or ascii_value == ord(' '): #check if the char is within A-Z character limit
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

    return ''.join(output)
            
def straight_european(text):
    i = 0
    output = []

    while i < len(text):
        ascii_value = ord(text[i])
        mod = ascii_value % 4
        if (ascii_value in range(ord('B'), Y_ascii) or ascii_value in range(ord('b'), y_ascii) or ascii_value == ord(' ')) and ascii_value != ord('w') and ascii_value != ord('W'):      #range B-X or b-x, without W or w
            
            if ascii_value == ord(' '):
                ascii_value += 4
            elif mod == 0:
                ascii_value -= 1
            elif mod == 1:
                ascii_value += 1
            elif mod == 2:
                ascii_value += 3
            else:
                ascii_value += 5

        elif ascii_value in [ ord('A'), ord('a'), ord('w'), ord('W'), y_ascii, Y_ascii, z_ascii, Z_ascii, ]:    #special cases, no pattern
            if ascii_value == ord('a'):
                ascii_value = ord('d')
            elif ascii_value == ord('A'):
                ascii_value = ord('D')
            elif ascii_value == ord('w'):
                ascii_value = ord('z')
            elif ascii_value == ord('W'):
                ascii_value = ord('Z')
            elif ascii_value == y_ascii:
                ascii_value = ord('b')
            elif ascii_value == Y_ascii:
                ascii_value = ord('B')
            elif ascii_value == z_ascii:
                ascii_value = ord('a')
            else:
                ascii_value = ord('A')

        else:
            raise ValueError(f'Error: "{chr(ascii_value)}" is not supported \nAlphabets are supported(A-Z or a-z) only')

        output.append(chr(ascii_value))
        i += 1

    return ''.join(output)

#print(straight_european("Ww"))
