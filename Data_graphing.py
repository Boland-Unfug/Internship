import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# read the data
df = pd.read_csv('Clean data/Cleaned_data.csv')

# get the total admissions
df['Total admissions'] = df['Members'] + df['Admissions/Covers']

# set the date to datetime, make date columns
df['date'] = pd.to_datetime(df['date'])
df['day'] = df['date'].dt.day
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year
df['month_day'] = df['date'].dt.strftime('%m-%d')
df['year_month'] = df['date'].dt.strftime('%Y-%m')
df['year_day'] = df['date'].dt.strftime('%Y-%j')

# create year dataframes
data_2022 = df[df['year'] == 2022]
data_2023 = df[df['year'] == 2023]
data_2024 = df[df['year'] == 2024]



# plot the data
sns.set(style='dark')
plt.figure(figsize=(15, 10))
sns.scatterplot(data=data_2022, x='month_day', y='Total admissions', label='2022')
sns.scatterplot(data=data_2023, x='month_day', y='Total admissions', label='2023')
sns.scatterplot(data=data_2024, x='month_day', y='Total admissions', label='2024')

plt.gca().xaxis.set_major_locator(plt.MaxNLocator(12))
plt.xticks(rotation=45)


plt.title('Total Admissions per Day')
plt.xlabel('Date')
plt.ylabel('Total Admissions')

plt.show()