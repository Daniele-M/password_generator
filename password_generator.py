import string
import random

def pass_gen(num, char):
    password = []

    for i in range(num):
        password.append(random.choice(char))

    print("".join(password))


LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATION = string.punctuation

pass_char = ""

print("You can have the default 16 character password with letters, numbers and punctuation by pressing 0.")

lenght = int(input("How long should the password be?\n"))

if lenght == 0:
    pass_gen(16, LETTERS + NUMBERS + PUNCTUATION)
elif lenght > 0:

    choice = input("Do you want letters in your password?\n")
    if "yes" in choice or "y" in choice:
        pass_char += LETTERS        

    choice = input("Do you want numbers in your password?\n")
    if "yes" in choice or "y" in choice:
        pass_char += NUMBERS

    choice = input("Do you want punctuation in your password?\n")
    if "yes" in choice or "y" in choice:
        pass_char += PUNCTUATION

    if pass_char == "":
        print("You must have some characters.")
        exit(0)
    pass_gen(lenght, pass_char)


else:
    print("Invalid number.")
    exit(0)
