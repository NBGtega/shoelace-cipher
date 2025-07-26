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

    return output

#def Lock():
#    print("Lock algo would go here")
#    print()

#def Gap():
#    print("Gap algo would go here")
#    print()

#crisscross("ABl")
