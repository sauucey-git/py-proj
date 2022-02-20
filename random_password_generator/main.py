# Simple program that generates random passwords
import random
import string

def genPassword() -> string:
    log = open("log.txt", "a")
    length = int(input("Length of password: "))
    characters = list(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)
    password = "".join(random.choices(characters, k=length))
    log.write(f"Password is {password}\n")
    log.close()
    return password


print(genPassword())