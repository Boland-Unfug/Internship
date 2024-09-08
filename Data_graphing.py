import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# read the data
df = pd.read_csv('Clean data/Cleaned_data.csv')

# get the Total Admissions
df['Total Admissions'] = df['Members'] + df['Admissions/Covers']

# set the date to datetime, make date columns
df['date'] = pd.to_datetime(df['date'])
df['day'] = df['date'].dt.day
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year
df['month_day'] = df['date'].dt.strftime('%m.%d')
df['year_month'] = df['date'].dt.strftime('%Y.%m')
df['year_day'] = df['date'].dt.strftime('%Y.%j')

# convert strings to numbers
df['month_day'] = pd.to_numeric(df['month_day'])
df['year_month'] = pd.to_numeric(df['year_month'])
df['year_day'] = pd.to_numeric(df['year_day'])

# create year dataframes
data_2022 = df[df['year'] == 2022]
data_2023 = df[df['year'] == 2023]
data_2024 = df[df['year'] == 2024]

#save the data
data_2022.to_csv('data/2022.csv', index=False)
data_2023.to_csv('data/2023.csv', index=False)
data_2024.to_csv('data/2024.csv', index=False)
















































#plot the data
# sns.set(style='dark')
# plt.figure(figsize=(15, 10))
# sns.scatterplot(data=df, x='date', y='Total Admissions')

# plt.gca().xaxis.set_major_locator(plt.MaxNLocator(6))

# plt.xticks(rotation=45)
# plt.title('Total Admissions per Day')
# plt.xlabel('Date')
# plt.ylabel('Total Admissions')

# plt.savefig('Graphs/Total Admissions Scatter.png')
# plt.show()



# plot the data so that it overlaps
# sns.set(style='dark')
# plt.figure(figsize=(15, 10))
# sns.scatterplot(data=data_2022, x='month_day', y='Total Admissions', label='2022')
# sns.scatterplot(data=data_2023, x='month_day', y='Total Admissions', label='2023')
# sns.scatterplot(data=data_2024, x='month_day', y='Total Admissions', label='2024')

# plt.gca().xaxis.set_major_locator(plt.MaxNLocator(12))
# plt.xticks(rotation=45)


# plt.title('Total Admissions per Day')
# plt.xlabel('Date')
# plt.ylabel('Total Admissions')

# plt.savefig('Graphs/Total Admissions Overlap Scatter.png')
# plt.show()

# # sum the data by month
# df_month = df.groupby('year_month')['Total Admissions'].sum()

# # plot the data by month
# sns.set(style='dark')
# plt.figure(figsize=(15, 10))
# sns.barplot(data=df_month, x='year_month', y='Total Admissions')

# plt.xticks(rotation=45)
# plt.title('Total Admissions per Month')
# plt.xlabel('Date')
# plt.ylabel('Total Admissions')

# # plt.savefig('Graphs/Total Admissions per Month.png')
# plt.show()