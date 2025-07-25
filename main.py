import string 
import matplotlib.pyplot as plt

letters = list(string.ascii_uppercase)

def first_pair(letters):
    shoe_lace_cordinates = {}
    for letter in range(7):
        left_letters = letters[letter * 2]
        right_letters = letters[letter * 2 + 1]
        shoe_lace_cordinates[left_letters] = (0,-letter)
        shoe_lace_cordinates[right_letters]= (1,-letter)
    
    return shoe_lace_cordinates
first_cordinate = first_pair(letters)
print(first_cordinate)

def second_pair(letters):
    for letter in range(7,23):
        shoe_lace_cordinates = {}
        left_letters = letters[letter * 2]
        right_letters = letters[letter * 2 + 1]
        shoe_lace_cordinates[left_letters] = (0,-letter)
        shoe_lace_cordinates[right_letters]= (1,-letter)
        return shoe_lace_cordinates

second_cordinate = second_pair(letters)
print(second_cordinate)
    


# plt.plot(shoe_lace_cordinates)
# for label, (x,y) in shoe_lace_cordinates.items():
#     plt.scatter(x,y)
#     plt.annotate(label,(x,y))



# plt.plot(shoe_lace_cordinates)

# plt.plot([1,2,3,4], [0.1,0.2,0.4,0.5])
# plt.ylabel('some numbers')
# plt.xlabel('some figures')
# plt.show()



# shoe_lace_cordinates = { 
#     "A": (0,0),
#     "B": (1,0),
#     "C": (0,-1),
#     "D": (1,-1),
#     "E": (0,-2),
#     "F": (1,-2),
#     "G": (0,-3),
#     "H": (1,-3),
#     "I": (0,-4),
#     "J": (1,-4),
#     "K": (0,-5),
#     "L": (1,-5),
#     "M": (0,-6),
#     "N": (1,-6),
#     "O": (0,-7),
#     "P": (1,-7),
#     "Q": (0,-8),
#     "R": (1,-8),
#     "S": (0,-9),
#     "T": (1,-9),
#     "U": (0,-10),
#     "V": (1,-10),
#     "W": (0,-11),
#     "X": (1,-11),
#     "Y": (0,-12),
#     "Z": (1,-12),
# }