#dattebayo
def crisscross(text):
    i = 0                                   #itereator
    list_of_char = list(text)               #list of input text
    output = []                             #output var
    while i < len(text):                    #runs till all characters are converted
        ascii_value = ord(list_of_char[i])  #ascii value of letter
        if ascii_value in range(ord('A'), ord('Z')):    #check if the char is within A-Z character limit
            if ascii_value % 2 == 0:            #check if it's even
                ascii_value += 1                #step of one char forward
            else:
                ascii_value += 3                #step of 3 char forward
            output.append(chr(ascii_value))     #appending after converting back to chr
            i += 1
        else:
            raise ValueError(f'Error: "{chr(ascii_value)}" is not supported \nUppercase letters (A-Z) are supported only')

    return "".join(output)


def army(text):
    i = 0                                   #itereator
                                            #list of input text
    output = []                             #output var

    while i < len(text):                    #runs till all characters are converted
        ascii_value = ord(text[i])  #ascii value of letter
        if ascii_value in range(ord('A'), ord('Z')): #check if the char is within A-Z character limit
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
            i += 1
        else:
            raise ValueError(f'Error: "{chr(ascii_value)}" is not supported \nUppercase letters (A-Z) are supported only')

    return "".join(output)
            
def straight_european(secret):
    print("Army algo would go here")
    print()
