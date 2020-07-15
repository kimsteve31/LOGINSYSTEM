# File: profile.py
# Date: 7/7/2020
# Author: Steve Kim
# Description: This file contains User profile data by accessing a csv file to store such data.

import pandas as pd

class UserProfile(object):

    def __init__(self):
        self.accounts = {}
        self.add_accounts()

    def get_accounts(self):
        """
        This function returns the variable accounts which contains a dictionary of username: password data
        :return: accounts
        """
        return self.accounts

    def getDataFile(self):
        """
        This function returns the DataFrame object for the userprofile.csv
        :return: DataFrame
        """
        return pd.read_csv('userprofile.csv')

    def add_accounts(self):
        """
        This function updates the accounts by reading through the excel file then adding users into the accounts dictionary
        :return: None
        """
        datafile = self.getDataFile()
        user_index = 0
        password_index = 1

        for index, row in datafile.iterrows():
            self.accounts[row[user_index]] = row[password_index]

    def register_account(self, username, password):
        """
        This function register the new account the was made in the register window
        :param username: Username for profile
        :param password: Password for profile
        :return: None
        """
        datafile = self.getDataFile()
        if username not in self.accounts:
            datafile.loc[len(datafile.index)] = [username, password]
            datafile.to_csv('userprofile.csv', index=False)
            self.add_accounts()
        else:
            print('WARNING: Username already taken! Try again.')

