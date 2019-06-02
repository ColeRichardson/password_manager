import sys
im


class Account:
    """holds the information for an account

    """
    def __init__(self, account_name, username, password):
        self.account_name = account_name
        self.username = username
        self.password = password
        #possibly email as well

    def get_password_strength(self):
        """returns the users password strength for the account
        :return:
        """
        pass

    def password_feedback(self):
        SPECIALS = ('!', '@', '#', '$')
        errors = []
        byte_condition = sys.getsizeof(self.password) <= 1024  # Sees the amount of bytes the password has
        digit_condition = False
        upper_condition = False
        length_condition = len(self.password) >= 8
        lower_condition = False
        specials_condition = False

        if not byte_condition:
            errors.append("Your password is way too long. Decrease its length.")

        if not length_condition:
            errors.append("Password is too short. Make it at least 8 characters or longer.")

        for character in self.password:

            if character.isdigit():
                digit_condition = True
            elif character.islower():
                lower_condition = True
            elif character.isupper():
                upper_condition = True
            elif character in SPECIALS:
                specials_condition = True

            true_condition = byte_condition and length_condition and digit_condition and upper_condition and \
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

        return errors

    def change_password(self):
        """changes the password for the account.
        :return:
        """
        pass

    def change_username(self):
        """changes the username for the account.
        :return:
        """
        pass

    def change_account_name(self):
        """changes the username for the account.
        :return:
        """
        pass

    def get_password(self):
        """gets the password for the account.

        :return:
        """
        pass

    def get_username(self):
        """gets the username for the account.

        :return:
        """
        pass

    def get_account_name(self):
        """gets the account_name for the account.

        :return:
        """
