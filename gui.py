import tkinter as tk
#import password_generator

class GUI:
    """ a gui for the password manager using tkinter
    """
    def __init__(self):
        """initializes the gui, sets up variables.

        self.status: 'register' or 'logon' or ''
        """
        self.root = tk.TK() #initialize tkinter root
        self.root.title = "Password Manager v0.1"

        self.account_list = [] # holds account objects in the Gui class
        self._status = 'register' # holds the status of what window we are in
        self.set_up_logon # prompt user with a button to ask to register

    def setup_register(self):
        """sets up the gui to prompt the user to register an account.

        :param self:
        :return:
        """
        pass

    def setup_logon(self):
        """
        sets up the gui for the logon window where user is prompted for username and password.
        checks if these are valid, if they are, run setup_main.
        :param self:
        :return:
        """
        pass

    def setup_main(self):
        """seets up the gui for the main windows of the application
        where the user can view all their passwords as buttons where the account name shows.

        :param self:
        :return:
        """
        pass

    def setup_account_info(self):
        """sets up the gui to display relevant information about the account
        :return:
        """

    def make_buttons(self):
        """creates the tkinter buttons

        :param self:
        :return:
        """
        Button1 = tk.button() #create a tkinter button

    def add_account(self):
        """create an account object for the username and password the user gave.
        also add the account object to the account_list

        :param self:
        :return:
        """

    def generate_password(self):
        """generates a password from password_generator.py

        :param self:
        :return:
        """
        pass





