import pandas as pd
import datetime
import calendar
import numpy as np
import os


# clean dataframe
clean_dataframe = pd.DataFrame()

# fill date range
start_date = datetime.date(2022,1,1)
end_date = datetime.date(2024,6,30)
date_range = pd.date_range(start_date, end_date)

clean_dataframe['date'] = date_range

def clean_data(df):
    # drop all rows except admissions/covers, members
    df = df.iloc[40:51]

    #find the rows with Members and return the row number
    #so the plan is to go through row by row to find the row with Members and the other ones
    df1 = df[df.apply(lambda row:row.astype(str).str.contains('Admissions/Covers').any(), axis=1)]
    df2 = df[df.apply(lambda row:row.astype(str).str.contains('Members').any(), axis=1)]
    df3 = df[df.apply(lambda row:row.astype(str).str.contains('Total Admissions').any(), axis=1)]
    # merge the two dataframes
    df = pd.concat([df1, df2, df3])

    # drop unnamed columns
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    
    # flip the dataframe
    df = df.T

    # reset the index
    df = df.reset_index()

    # drop the first and second row
    df = df.drop([0,1])
    
    # rename the columns
    df.columns = ['index', 'Admissions/Covers', 'Members', 'Total Admissions']

    # drop the first column
    df = df.drop('index', axis=1)

    # reset the index
    df = df.reset_index()

    # drop the first column (again)
    df = df.drop('index', axis=1)

    return df


# get the file name for the excel files
path = 'Raw data'
files = os.listdir(path)
files = [file for file in files if file.endswith('.xlsx')]
temp = pd.DataFrame()
for file in files:
    print(file)
    df = pd.ExcelFile('Raw data/' + file)
    df = df.parse('Pool')
    df = clean_data(df)
    # concatinate the dataframes
    temp = pd.concat([temp, df], axis=0)

print(temp)

# reset the index
temp = temp.reset_index()

# drop the first column (again)
temp = temp.drop('index', axis=1)

# print(temp)

# merge the dataframes
clean_dataframe = pd.concat([clean_dataframe, temp], axis=1)

print(clean_dataframe)

#SAVE THIS DOC
clean_dataframe.to_csv('clean_data.csv', index=False)
