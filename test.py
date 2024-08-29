import pandas as pd
import datetime
import calendar
import numpy as np

# clean dataframe
clean_data = pd.DataFrame()

# fill date range
start_date = datetime.date(2022,1,1)
end_date = datetime.date.today()
date_range = pd.date_range(start_date, end_date)

clean_data['date'] = date_range

def clean_data(df):
    # drop all rows except admissions/covers, members
    df = df.iloc[[46,47]]
    # drop unnamed columns
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    return df


# get the file name for the excel files






# read all excel files in the Raw Data folder

# read the first excel file                                                                                         
df = pd.ExcelFile('Raw data/DIJ - 01.2022.xlsx')
print(df.sheet_names)
df1 = df.parse('Pool')
print(df1)
df2 = clean_data(df1)
print(df2)



