from random import randint
import hashlib


def password_generator(length):
    UPPERCASE = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                 'Y', 'Z')

    SPECIALS = ('!', '@', '#', '$')

    password = ""

    for _ in range(length):

        if randint(0, 1) or not len(password):  # 'not len(password)' makes sure the first character is part of the
            if randint(0, 1):                   # alphabet
                password += UPPERCASE[randint(0, len(UPPERCASE) - 1)].lower()
            else:
                password += UPPERCASE[randint(0, len(UPPERCASE) - 1)]

        else:
            if randint(0, 1):
                password += str(randint(0, 9))
            else:
                password += SPECIALS[randint(0, len(SPECIALS) - 1)]

    return password


def encrypt(password: str):
    salt = b"71ec511e2d81a2eba596dba5ce25b5bb3ac0df3278adc7beaa0fa961366fb7c7"  # Used to secure the password encryption
    password = password.encode("utf-8")  # Turns the string password into bytes
    return hashlib.pbkdf2_hmac('sha512', password, salt, 100000).hex()  # Encrypts the password using SHA512


if __name__ == "__main__":
    print(encrypt(password_generator(8)))
