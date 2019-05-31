from random import randint
import hashlib


def password_generator(length):

    UPPERCASE = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                 'Y', 'Z')

    SPECIALS = ('!', '@', '#', '$')

    password = ""

    for _ in range(length):

        if randint(0, 1) or not len(password):
            if randint(0, 1):
                password += UPPERCASE[randint(0, len(UPPERCASE) - 1)].lower()
            else:
                password += UPPERCASE[randint(0, len(UPPERCASE) - 1)]

        else:
            if randint(0, 1):
                password += str(randint(0, 9))
            else:
                password += SPECIALS[randint(0, len(SPECIALS) - 1)]

    return password


def encrypt(password):
    


if __name__ == "__main__":
    while True:
        print(password_generator(int(input("Please enter the length of the Password\n"))))
