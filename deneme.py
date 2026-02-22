import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>abcdefguhijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

