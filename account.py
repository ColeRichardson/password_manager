import sys
import verbs, nouns, adjectives, adverbs
import copy


class Account:
    """holds the information for an account

    """
    def __init__(self, account_name, username, password):
        self.account_name = account_name
        self.username = username
        self.password = password
        #possibly email as well

    def get_password_strength(self, score=None, password=None):
        """returns the users password strength for the account
        :return:
        """

        common_words = verbs + nouns + adjectives + adverbs
        alpha_pattern = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        num_pattern = "0123456789876543210"
        score = score if score else 0
        password = password if password else copy.deepcopy(self.password)
        phrase = password[:2]

        for character in password[2:]:

            condition1 = (phrase in common_words) or (phrase in num_pattern)
            condition2 = (phrase in alpha_pattern) or (phrase in reversed(alpha_pattern))

            if condition1 or condition2:
                score -= 1
                return score + self.get_password_strength(score=score, password=password.replace(phrase, ""))

            phrase += character

        return score

    def password_feedback(self):
        SPECIALS = ('!', '@', '#', '$')
        feedback = []
        byte_condition = sys.getsizeof(self.password) <= 1024  # Sees the amount of bytes the password has
        digit_condition = False
        upper_condition = False
        length_condition = len(self.password) >= 8
        lower_condition = False
        specials_condition = False

        if not byte_condition:
            feedback.append("Your password is way too long. Decrease its length.")

        if not length_condition:
            feedback.append("Password is too short. Make it at least 8 characters or longer.")

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
            feedback.append("Add a numerical digit to your password.")
        if not upper_condition:
            feedback.append("The password must have an upper-case letter.")
        if not lower_condition:
            feedback.append("The password must have a lower-case letter.")
        if not specials_condition:
            feedback.append("The Password must have a special character: '!@#$'.")

        return feedback

    def change_password(self, old_password, new_password):
        """changes the password for the account.
        :return:
        """
        pass

    def change_username(self, new_username, password):
        """changes the username for the account.
        :return:
        """
        pass

    def change_account_name(self, new_acount_name, password):
        """changes the username for the account.
        :return:
        """
        pass

    def get_password(self):
        """gets the password for the account.

        :return:
        """
        return self.password

    def get_username(self):
        """gets the username for the account.

        :return:
        """
        return self.username

    def get_account_name(self):
        """gets the account_name for the account.

        :return:
        """
        return self.account_name
