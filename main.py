# import string
import os, time
from shoe_lacing_algos import *
import argparse
# import matplotlib.pyplot as plt

# letters = list(string.ascii_uppercase)

# def first_pair(letters):
#     shoe_lace_cordinates = {}
#     for letter in range(7):
#         left_letters = letters[letter * 2]
#         right_letters = letters[letter * 2 + 1]
#         shoe_lace_cordinates[left_letters] = (0,-letter)
#         shoe_lace_cordinates[right_letters]= (1,-letter)
    
#     return shoe_lace_cordinates
# first_cordinate = first_pair(letters)
# print(first_cordinate)

# def second_pair(letters):
#     for letter in range(7,23):
#         shoe_lace_cordinates = {}
#         left_letters = letters[letter * 2]
#         right_letters = letters[letter * 2 + 1]
#         shoe_lace_cordinates[left_letters] = (0,-letter)
#         shoe_lace_cordinates[right_letters]= (1,-letter)
#     return shoe_lace_cordinates

# second_cordinate = second_pair(letters)
# print(second_cordinate)
    


# # plt.plot(shoe_lace_cordinates)
# # for label, (x,y) in shoe_lace_cordinates.items():
# #     plt.scatter(x,y)
# #     plt.annotate(label,(x,y))



# # plt.plot(shoe_lace_cordinates)

# # plt.plot([1,2,3,4], [0.1,0.2,0.4,0.5])
# # plt.ylabel('some numbers')
# # plt.xlabel('some figures')
# # plt.show()



# # shoe_lace_cordinates = { 
# #     "A": (0,0),
# #     "B": (1,0),
# #     "C": (0,-1),
# #     "D": (1,-1),
# #     "E": (0,-2),
# #     "F": (1,-2),
# #     "G": (0,-3),
# #     "H": (1,-3),
# #     "I": (0,-4),
# #     "J": (1,-4),
# #     "K": (0,-5),
# #     "L": (1,-5),
# #     "M": (0,-6),
# #     "N": (1,-6),
# #     "O": (0,-7),
# #     "P": (1,-7),
# #     "Q": (0,-8),
# #     "R": (1,-8),
# #     "S": (0,-9),
# #     "T": (1,-9),
# #     "U": (0,-10),
# #     "V": (1,-10),
# #     "W": (0,-11),
# #     "X": (1,-11),
# #     "Y": (0,-12),
# #     "Z": (1,-12),
# # }


def main():
    print("Welcome to the shoelace-cipher")
    print("Your trusty CLI to cypher your secrets ;)")
    print()
    print("If you need more information you can use the flag --help")

    active = True

    while active:
        #This creates an ArgumentParser object. It detects the flags automagically. Also, you can set it up to have the flags
        # that you want. It also omits the step of having to check if the input is in the algos dictionary.
        # Idk if we are going to use something like this, but at least it's a start ;) 
        parser = argparse.ArgumentParser(description="This CLI helps you cypher" \
        "your secrets with a shoe-lacing algorithm of your choosing", usage="main.py [method]")

        #Here you set up your own flags. The required argument is important because you are saying
        #that this flag cannot be omitted.
        parser.add_argument("-m", "--method", metavar="method", required=True, choices=["criss-cross", "gap", "lock"],
                            help="Shoe-lacing method the user wants")
        
        #This reads the arguments passed to the terminal
        args = parser.parse_args()

        method = args.method 

        #I think here we can call the logic and pass the relevant arguments
        print(method) 

        time.sleep(3)

        break

    os.system("clear")

        

if __name__== "__main__":
    main()