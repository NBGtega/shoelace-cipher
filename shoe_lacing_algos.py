def crisscross(secret):
    #This is a hand written graph with where to each word points to
    #It is super inefficient
    word_graph= {
        "a":"d",
        "b":"c",
        "c":"f",
        "d":"e",
        "e":"h",
        "f":"g",
        "g":"j",
        "h":"i",
        "i":"l",
        "j":"k",
        "k":"n",
        "l":"m",
        "m":"p",
        "n":"o",
        "o":"r",
        "p":"q",
        "q":"t",
        "r":"s",
        "s":"v",
        "t":"u",
        "u":"x",
        "v":"w",
        "w":"z",
        "x":"y",
        "y":"y",
        "z":"z"
    }
    #My logic is, we check each word to a key in the dict and add it's value to the list
    cyphered_secret = []
    for l in secret:
        cyphered_secret.append(word_graph[l])

    return "".join(cyphered_secret)
    


def straight_european(secret):
    print("straight_european algo would go here")
    print()

def army(secret):
    print("Army algo would go here")
    print()
