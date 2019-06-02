from random import randint
import hashlib
import sys


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


def password_inspector(password: str):
    SPECIALS = ('!', '@', '#', '$')
    errors = []
    byte_condition = sys.getsizeof(password) <= 1024  # Sees the amount of bytes the password has
    digit_condition = False
    upper_condition = False
    length_condition = len(password) >= 8
    lower_condition = False
    specials_condition = False

    if not byte_condition:
        errors.append("Your password is way too long. Decrease its length.")

    if not length_condition:
        errors.append("Password is too short. Make it at least 8 characters or longer.")

    for character in password:

        if character.isdigit():
            digit_condition = True
        elif character.islower():
            lower_condition = True
        elif character.isupper():
            upper_condition = True
        elif character in SPECIALS:
            specials_condition = True

        true_condition = byte_condition and length_condition and digit_condition and upper_condition and\
                         lower_condition and specials_condition

        if true_condition:
            return "That's a perfect password."

    if not digit_condition:
        errors.append("Add a numerical digit to your password.")
    if not upper_condition:
        errors.append("The password must have an upper-case letter.")
    if not lower_condition:
        errors.append("The password must have a lower-case letter.")
    if not specials_condition:
        errors.append("The Password must have a special character: '!@#$'.")

    if not errors:
        return "\n".join(errors)


if __name__ == "__main__":
    print(encrypt(password_generator(8)))
