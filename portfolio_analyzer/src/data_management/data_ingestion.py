import pandas as pd
import re

# Actual data to work with, loaded from external csv file.
root_df = pd.read_csv("data_dir/raw_transactions.csv")

"""
    Following functions to perform:
    1. Raw strings of dates converted to datetime objects
    2. Handling Nulls: NaN values replaced with '0.0'
    3. String Parsing with Regex
"""

def datetime_conversion():
    global root_df
    root_df["Timestamp"] = pd.to_datetime(root_df["Timestamp"])

def nan_manage():
    global root_df
    root_df["Tx_Fee"] = root_df["Tx_Fee"].fillna(0.0)

def parsing_regex():
    global root_df
