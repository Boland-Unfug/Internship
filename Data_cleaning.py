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

    # # rows to drop: 0, 1, 36-39
    df = df.drop([0,1])
    df = df.drop(df.index[31:40])

    df = df.reset_index(drop=True)

    # rename the columns
    df.columns = ['index', 'Admissions/Covers', 'Members']

    # drop the index column
    df = df.drop(columns=['index'])

    # fill the NaN and NaT values with 0
    df = df.fillna(0)

    # add the total admissions column
    df['Total Admissions'] = df['Members'] + df['Admissions/Covers']

    return df

def add_date(df, file):
    # get the date from the file name
    date = file.split(' - ')[1].split('.xlsx')[0]

    # get the month and year
    year = date.split('.')[0]
    month = date.split('.')[1]

    # get the number of days in the month
    num_days = len(df)

    # create the date column
    df['date'] = pd.date_range(start=date, periods=num_days)
    
    # drop row if it does not match the month
    df = df.drop(df[df['date'].dt.month != int(month)].index)

    # set the date as the index
    df = df.set_index('date', append=False)

    return df

# clean dataframe
clean_dataframe = pd.DataFrame()

# get the files
path = 'Raw data'
files = os.listdir(path)
files = [file for file in files if file.endswith('.xlsx')]


for file in files:

    # read the file and fix the data
    df = pd.ExcelFile ('Raw data/' + file)
    df = df.parse('Pool')
    df = clean_data(df)
    df = add_date(df, file)


    # delete the file if it already exists
    if os.path.exists('data/' + str(file) + '.csv'):
        os.remove('data/' + str(file) + '.csv')

    # drop the extra stuff from the file name
    file = file.split('.xlsx')[0]
    file = file.split(' - ')[1]
    df.to_csv('data/' + str(file) + '.csv', index=True)

    # append the dataframe to the clean dataframe
    clean_dataframe = pd.concat([clean_dataframe, df])
    
# delete the file if it already exists
if os.path.exists('data/Cleaned_data.csv'):
    os.remove('data/Cleaned_data.csv')
clean_dataframe.to_csv('data/Cleaned_data.csv', index=True)

# save the data by year
data_2022 = clean_dataframe.loc['2022']
data_2023 = clean_dataframe.loc['2023']
data_2024 = clean_dataframe.loc['2024']

# delete the file if it already exists
if os.path.exists('data/2022.csv'):
    os.remove('data/2022.csv')
data_2022.to_csv('data/2022.csv', index=True)

# delete the file if it already exists
if os.path.exists('data/2023.csv'):
    os.remove('data/2023.csv')
data_2023.to_csv('data/2023.csv', index=True)

# delete the file if it already exists
if os.path.exists('data/2024.csv'):
    os.remove('data/2024.csv')
data_2024.to_csv('data/2024.csv', index=True)
