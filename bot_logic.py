import random


def gen_pass(pass_length):
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def moneda():
    giro = random.randint(0, 2)
    if giro == 0:
        return "cara"
    else:
        return "sol"
 
