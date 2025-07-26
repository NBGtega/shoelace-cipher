# import string
import os, time
from shoe_lacing_algos import *
import argparse

algos = {"criss-cross": crisscross,
         "straight european": straight_european,
         "army": army}


def main():
    print("Welcome to the shoelace-cipher")
    print("Your trusty CLI to cypher your secrets ;)")
    print()
    print("Supported cyphering methods: criss-cross, straight european, army")
    print("If you need more information you can use the flag --help")

    active = True

    while active:
        #This creates an ArgumentParser object. It detects the flags automagically. Also, you can set it up to have the flags
        # that you want. It also omits the step of having to check if the input is in the algos dictionary.
        # Idk if we are going to use something like this, but at least it's a start ;) 
        parser = argparse.ArgumentParser(description="This CLI helps you cypher" \
        "your secrets with a shoe-lacing algorithm of your choosing", usage="main.py [secret] [method]")

        #This flag is going to contain the secret we are going to be cyphering.
        parser.add_argument("-s", "--secret", metavar="secret", required=True,
                            help="The secret you want to cypher")

        #Here you set up your own flags. The required argument is important because you are saying
        #that this flag cannot be omitted.
        parser.add_argument("-m", "--method", metavar="method", required=True, choices=["criss-cross",
                            "straight european", "army"], help="Shoe-lacing method the user wants")
        
        #This reads the arguments passed to the terminal
        args = parser.parse_args()

        method = args.method
        secret_word = args.secret
        secret_divided= []
        
        #To avoid having to divide the word in each aglo function, we pass it already divided
        for l in secret_word:
            secret_divided.append(l)

        #We repeat the process three times to make it as difficult as possible to crack (?)
        first_round = algos[method](secret_divided)
        second_round = algos[method](first_round)
        third_round = algos[method](second_round)

        print(first_round)
        print(second_round)
        print(third_round)

        #We can convert it here to hexadecimal and it might add another layer
        
        time.sleep(5)

        break

    os.system("clear")

        

if __name__== "__main__":
    main()