import argparse
from shoe_lacing_algos import crisscross, army, straight_european
from helper_func import reverse, hex_for_str, xor_encrypt_hex, xor_decrypt_hex

algos = {"cc": crisscross,
         "se": straight_european,
         "a": army}


def main():
    print("Welcome to the shoelace-cipher")
    #print("Your trusty CLI to cypher your secrets ;)")
    print("\n")

    #This creates an ArgumentParser object. It detects the flags automagically. Also, you can set it up to have the flags
    # that you want. It also omits the step of having to check if the input is in the algos dictionary. 
    parser = argparse.ArgumentParser(description="This CLI helps you cypher " \
    "your secrets with a shoe-lacing algorithm of your choice. " \
    # "Use --help for more info. " remoevd this string as it prints when using the --help flag too
    "Supported cyphering methods: criss-cross(cc), straight_european(se), army(a). ", usage="main.py [message] [method]")

    #We create here a group of mutually exclusive flags
    group = parser.add_mutually_exclusive_group(required=True)

    #This flag is for the encryption method
    group.add_argument("-e", "--en", metavar="algorithm", dest="algorithm", choices=["cc",
                        "se", "a"], help="Shoe-lacing encryption method")

    #This flag contains the magic key to encrypt
    #Because we use nargs='+' this is going to return a list we need to convert to string 
    group.add_argument("-k", "--key",metavar="encryption_key", dest="encrypt_key", nargs='+',
                        help="Magic key to encrypt the message with")

    group.add_argument("-d", "--decrypt", metavar="decryption_key", dest="decrypt_key", nargs='+',
                       help="Decrypts encrypted message,(currently only decrypts encrypted with -k flag). Parse magic key with which message was encrypted")
    
    
    #This flag is going to contain the secret we are going to be cyphering.
    #Because we use nargs='+' this is going to return a list we need to convert to string
    parser.add_argument("-m", "--msg", dest="message", required=True, nargs='+',
                        help="The message you want to encrypt")
    
    
    #This reads the arguments passed to the terminal
    args = parser.parse_args()

    en_method = args.algorithm #this is a list
    msg = list(args.message)
    encrypt_key = args.encrypt_key
    decrypt_key = args.decrypt_key
    
    if encrypt_key is not None: #To pass this value, we need to convert it to a string
       xor_encryption = xor_encrypt_hex("".join(msg), "".join(encrypt_key))
       print(f"Output:{xor_encryption}")

    elif decrypt_key is not None:
        xor_decryption = xor_decrypt_hex("".join(msg), "".join(decrypt_key))
        print(f"Output:{xor_decryption}")

    #We repeat the process three times to make it as difficult as possible to crack (?)
    elif en_method is not None:
        first_round = algos[en_method]("".join(msg))
        second_round = algos[en_method](first_round)
        third_round = algos[en_method](second_round)
        inverted = reverse(third_round)
        hexed = hex_for_str(second_round)
        final = ""
        i = 0
        
        while i < len(third_round):
            if i % 2 == 0:
                final += inverted[i]
            else:
                final += hexed[i]
            i += 1
        print(f"Output:{final}")
    #We can convert it here to hexadecimal and it might add another layer
        


        

if __name__== "__main__":
    main()
