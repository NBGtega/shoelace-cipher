from shoe_lacing_algos import crisscross, army, straight_european
from helper_func import check

text_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
text_lower = text_upper.lower()

def recurse(text="ABC", recursion=0): #constantly encrypts with algorithm repepatedly and slaps in your face if it gives original string in 300 recursions range
    if recursion >= 300:
        print("We're safe(for now)")
        return 
    recursion += 1
    if text == "ABC" and recursion != 1:
        print(f"We're fked after {recursion} recursions")
        return
    recurse(crisscross(text), recursion)


def check_criss_cross():
    expected_upper = "DCFEHGJILKNMPORQTSVUXWZYBA"
    expected_lower = expected_upper.lower()
    actual_upper = crisscross(text_upper)
    actual_lower = crisscross(text_lower)

    print("Checking crisscross algorithm...")
    check(expected_lower, actual_lower, expected_upper, actual_upper)

def check_army():
       expected_upper = "CDFEGHJIKLNMOPRQSTVUWXZYAB"
       expected_lower = "cdfeghjiklnmoprqstvuwxzyab"
       actual_upper = army(text_upper)
       actual_lower = army(text_lower)

       print("Checking army algorithm...")
       check(expected_lower, actual_lower, expected_upper, actual_upper)


def check_str_eur():
    expected_upper = "DEHCFILGJMPKNQTORUXSVYZWBA"
    expected_lower = expected_upper.lower()
    actual_upper = straight_european(text_upper)
    actual_lower = straight_european(text_lower)

    print("Checking straight_european algorithm...")
    check(expected_lower, actual_lower, expected_upper, actual_upper)


#check_army() 
#check_criss_cross()
#check_str_eur()
