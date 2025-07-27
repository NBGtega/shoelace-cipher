from shoe_lacing_algos import crisscross, army, straight_european

text_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
text_lower = text_upper.lower()

def cause(expected, actual):
    i = 0
    expected_list = []
    errored_list = []

    while i < len(expected):
        if expected[i] != actual[i]:
            expected_list.append(expected[i])
            errored_list.append(actual[i])
        i += 1

    i = 0
    print("Bug(s) found!")        
    while i < len(expected_list):
        print(f"Expected: {expected_list[i]}        Actual: {errored_list[i]}")
        i += 1

def check_criss_cross():
    expected_upper = "DCFEHGJILKNMPORQTSVUXWZYBA"
    expected_lower = expected_upper.lower()
    actual_upper = crisscross(text_upper)
    actual_lower = crisscross(text_lower)
    print("Checking crisscross algorithm...")

    if actual_upper == expected_upper:
        print("Passed uppercase test")
    else:
        print("Failed uppercase test")
        cause(expected_upper, actual_upper)

    if actual_lower == expected_lower:
        print("Passed lowercase")
    else:
        print("Failed lowercase test")
        cause(expected_lower, actual_lower)

def check_army():
       expected_upper = "CDFEGHJIKLNMOPRQSTVUWXZYAB"
       expected_lower = "cdfeghjiklnmoprqstvuwxzyab"
       actual_upper = army(text_upper)
       actual_lower = army(text_lower)
       print("Checking army algorithm...")

       if actual_upper == expected_upper:
           print("Passed uppercase test")
       else:
            print("Failed uppercase test")
            cause(expected_upper, actual_upper)

       if actual_lower == expected_lower:
            print("Passed lowercase")
       else:
            print("Failed lowercase test")
            cause(expected_lower, actual_lower)

#check_army() currently giving errors due to incomplete logic 
check_criss_cross()
