import pandas as pd
import datetime
import calendar
import numpy as np
import os


# clean dataframe
clean_data = pd.DataFrame()

# fill date range
start_date = datetime.date(2022,1,1)
end_date = datetime.date.today()
date_range = pd.date_range(start_date, end_date)

clean_data['date'] = date_range

def clean_data(df):
    # drop all rows except admissions/covers, members
    df = df.iloc[40:50]

    #find the rows with Members and return the row number
    #so the plan is to go through row by row to find the row with Members and the other ones
    df1 = df[df.apply(lambda row:row.astype(str).str.contains('Admissions/Covers').any(), axis=1)]
    df2 = df[df.apply(lambda row:row.astype(str).str.contains('Members').any(), axis=1)]

    # merge the two dataframes
    df = pd.concat([df1, df2])
    # print(df)
    # drop unnamed columns
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    
    # flip the dataframe
    df = df.T
    # reset the index
    df = df.reset_index()

    # drop the first and second row
    df = df.drop([0, 1])

    # drop the first column
    df = df.drop('index', axis=1)

    # reset the index
    df = df.reset_index()

    # drop the first column (again)
    df = df.drop('index', axis=1)

    # rename the columns
    df.columns = ['Admissions/Covers', 'Members']
    return df


# get the file name for the excel files
path = 'Raw data'
files = os.listdir(path)
files = [file for file in files if file.endswith('.xlsx')]

for file in files:
    print(file)
    df = pd.ExcelFile('Raw data/' + file)
    df = df.parse('Pool')
    df = clean_data(df)
    # add 46 to clean_data as non-members
    # clean_data[file + ' non-members'] = df2[46]



