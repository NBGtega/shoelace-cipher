import argparse
from shoe_lacing_algos import crisscross, army, straight_european
from helper_func import reverse, hex_for_str

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
    "Supported cyphering methods: criss-cross(cc), straight_european(se), army(a). " \
    "Use --help for more info. ", usage="main.py [secret] [method]")

    #We create here a group of mutually exclusive flags
    group = parser.add_mutually_exclusive_group(required=True)

    #This flag is for the encryption method
    group.add_argument("-e", "--en", metavar="algorithm", dest="algorithm", choices=["cc",
                        "se", "a"], help="Shoe-lacing encryption methods")

    #This flag contains the magic key to encrypt
    #Because we use nargs='+' this is going to return a list we need to convert to string 
    ##group.add_argument("-k", "--key", metavar="magic_key", dest="magic_key", nargs='+',
    ##                    help="Magic key to encrypt the message with")
    
    
    #This flag is going to contain the secret we are going to be cyphering.
    #Because we use nargs='+' this is going to return a list we need to convert to string
    parser.add_argument("-m", "--msg", metavar="message", dest="message", required=True, nargs='+',
                        help="The secret you want to cypher")
    
    
    #This reads the arguments passed to the terminal
    args = parser.parse_args()

    en_method = args.algorithm #this is a list
    msg_to_encrypt = list(args.message)
    #magic_value= args.magic_key #This is a list

    #if magic_value != None: #To pass this value, we need to convert it to a string
    #   xor_encryption = xor("".join(msg_to_encrypt), "".join(magic_value))
    #   print(xor_encryption)

    #We repeat the process three times to make it as difficult as possible to crack (?)
    if en_method != None:
        first_round = algos[en_method]("".join(msg_to_encrypt))
        second_round = algos[en_method](first_round)
        third_round = algos[en_method](second_round)
        inverted = reverse(third_round)
        hexed = hex_for_str(inverted)
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
