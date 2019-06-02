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
