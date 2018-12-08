#!/usr/bin/env python3
"""
sheets.py - View database using Google Sheets

See: https://gspread.readthedocs.io/en/latest/
"""

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build

from constants import Constants
import utils


def create_db():
    db = GoogleSheetsDB('instagram-data', 'photos')

    return db


class GoogleSheetsDB(object):
    """
    Use a single worksheet in a spreadsheet as a database
    """

    def __init__(self, spreadsheet, worksheet='sheet1'):
        """
        """
        self.login()
        self.get_spreadsheet(spreadsheet)
        self.get_worksheet(worksheet)

    def login(self):
        """
        """
        scope = [Constants.GOOGLE_SHEETS, Constants.GOOGLE_DRIVE]
        path = utils.find_file('client_secret.json')
        creds = ServiceAccountCredentials.from_json_keyfile_name(path, scope)
        self.client = gspread.authorize(creds)

    def get_spreadsheet(self, spreadsheet_name):
        """
        """
        try:
            self.spreadsheet = self.client.open(spreadsheet_name)
        except:
            self.spreadsheet = self.client.create(spreadsheet_name)
            self.spreadsheet.share('kothary.vikash@gmail.com', perm_type='user', role='owner')
            self.spreadsheet.share('tej780@hotmail.co.uk', perm_type='user', role='writer')

    def get_worksheet(self, worksheet_name):
        """
        """
        try:
            self.worksheet = self.spreadsheet.worksheet(worksheet_name)
        except:
            self.worksheet = self.spreadsheet.add_worksheet(
                title=worksheet_name, rows="100", cols="20")

    def set_headers(self, header_names):
        """
        """
        self.worksheet.delete_row(1)
        self.worksheet.insert_row(header_names, 1)

    # def load_csv(self):
    #     """
    #     WARNING: This will overrite the worksheet.
    #     """
    #     content = open('data/ids.csv', 'r').read()
    #     self.client.import_csv(self.spreadsheet.id, content)

    def save(self, data):
        self.worksheet.append_row(data)
