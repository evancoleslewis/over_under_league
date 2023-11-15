import gspread
from gspread import Client
import gspread_dataframe
import pandas as pd
import config
import logging

def load_to_gsheet(df, sheet_name):

    gc = gspread.service_account()

    spreadsheet = gc.open_by_url(config.GSHEET_URL)
    logging.info('Accessed the Google Sheet')
    worksheet = spreadsheet.worksheet(sheet_name)
    worksheet.clear()

    gspread_dataframe.set_with_dataframe(worksheet, df)
    logging.info('Uploaded data to worksheet: {sheet_name}}')

    return
