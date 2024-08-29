import pandas as pd
    import datetime
    import calendar
    import numpy as np
    
# clean dataframe
clean_data = pd.DataFrame(columns=['date','admissions','members','non-members'])
print(clean_data)

def fill_dates(df):
    # now fill the date column wwith the dates from january of 2022 to today

    start_date = datetime.date(2022,1,1)
    end_date = datetime.date.today()
    date_range = pd.date_range(start_date, end_date)
    print(date_range)

    # now fill the date column with the date range
    df['date'] = date_range
    print(df)


# now fill the date column with the date range
clean_data['date'] = date_range
print(clean_data)


def clean_data(df):
    # drop all rows except admissions/covers, members
    df = df.iloc[[46,47]]
    # drop unnamed columns, POOL column
    df = df.drop(['POOL'], axis=1)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    return df


def get_data(file):
    # read the first excel file                                                                                         
    df = pd.ExcelFile(file)
    print(df.sheet_names)
    df1 = df.parse('Pool')
    print(df1)
    df2 = clean_data(df1)
    print(df2)
    return df2


get_data('Raw data/DIJ - 01.2022.xlsx')



