import pandas as pd
import datetime
import calendar
import numpy as np
import os


def clean_data(df):
    # drop all rows except admissions/covers, members
    df = df.iloc[44:51]

    #find the rows with Members and return the row number
    #so the plan is to go through row by row to find the row with Members and the other ones
    df1 = df[df.apply(lambda row:row.astype(str).str.contains('Admissions/Covers').any(), axis=1)]
    df2 = df[df.apply(lambda row:row.astype(str).str.contains('Members').any(), axis=1)]

    # merge the dataframes
    df = pd.concat([df1, df2])

    # flip the dataframe
    df = df.T

    # reset the index
    df = df.reset_index()

    # rows to drop: 0, 1, 36-39
    df = df.drop([0,1])
    df = df.drop(df.index[31:40])
    
    # rename the columns
    df.columns = ['index', 'Admissions/Covers', 'Members']

    # drop the first column
    df = df.drop('index', axis=1)

    # reset the index
    df = df.reset_index()

    # drop the first column (again)
    df = df.drop('index', axis=1)

    # fill the NaN and NaT values with 0
    df = df.fillna(0)

    return df

# clean dataframe
clean_dataframe = pd.DataFrame()

path = 'Raw data'
files = os.listdir(path)
files = [file for file in files if file.endswith('.xlsx')]

for file in files:

    df = pd.ExcelFile ('Raw data/' + file)
    df = df.parse('Pool')
    df = clean_data(df)

    # get the start date from the file name
    file = file[6:]
    file = file[:-5]
    file = file.split('.')
    start_date = datetime.date(int(file[0]), int(file[1]), 1)
    print(start_date)

    # fill the date range for that month
    date_range = pd.date_range(start_date, periods=len(df), freq='D')
    df['date'] = date_range

    # drop the rows where the month is not the same as the month in the file name
    df.drop(df[df['date'].dt.month != start_date.month].index, inplace=True)
    print(df)

    # change the name of the file to the date
    file = str(start_date)
        # delete the file if it already exists
    if os.path.exists('Clean data/' + str(file) + '.csv'):
        os.remove('Clean data/' + str(file) + '.csv')
    df.to_csv('Clean data/' + str(file) + '.csv', index=False)

    # append the dataframe to the clean dataframe
    clean_dataframe = pd.concat([clean_dataframe, df])
    
# save the clean dataframe
clean_dataframe.to_csv('Clean data/Cleaned_data.csv', index=False)



