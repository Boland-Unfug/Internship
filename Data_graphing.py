import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import regression_poly as reg

# read in the three year files of data
data_2022 = pd.read_csv('data/Cleaned_data_2022.csv')
data_2023 = pd.read_csv('data/Cleaned_data_2023.csv')
data_2024 = pd.read_csv('data/Cleaned_data_2024.csv')

def lin_reg(data):
    X_headers = ['index']
    X = data.index.values
    X = X.reshape(-1, 1)
    Y_header = 'Total Admissions'
    Y = data['Total Admissions']
    degree = 1
    best_r_sq = 0
    #find the r^2 that is closest to 1
    for i in range(1, 10):
        W, r_sq_test, rmse_test, r_sq_train, rmse_train = reg.model_poly( X, X_headers, Y, Y_header, degree=i, title="Polynomial Model", draw=False)
        if r_sq_test > best_r_sq and r_sq_test < 1 and r_sq_test > 0.5:
            best_r_sq = r_sq_test
            degree = i

    # save the graph
    W, r_sq_test, rmse_test, r_sq_train, rmse_train = reg.model_poly( X, X_headers, Y, Y_header, degree=degree, title="Polynomial Model", draw=False)
    return W, degree

# plot the data so that it overlaps
sns.set(style='dark')
plt.figure(figsize=(15, 10))

for data in [data_2022, data_2023, data_2024]:

    # Get the best degree and weights for the data
    W, degree = lin_reg(data)  # Assuming this function gives the best polynomial degree and weights

    # Create the input matrix based on 'Total Admissions'
    new_data = data.index.values.reshape(-1, 1)

    # Build the polynomial input matrix
    input_matrix = reg.build_input_matrix_poly(new_data, degree)  # Make sure this captures polynomial terms correctly

    # Predict using the learned weights
    data['Total Admissions Prediction'] = reg.predict(input_matrix, W)

    # Plot actual vs predicted for this dataset
    sns.scatterplot(data=data, x=data.index, y='Total Admissions', label=)  # Scatter plot for actual data
    sns.lineplot(data=data, x=data.index, y='Total Admissions Prediction')  # Line plot for predicted data


plt.gca().xaxis.set_major_locator(plt.MaxNLocator(12))
plt.xticks(rotation=45)

plt.title('Total Admissions per Day')
plt.xlabel('Date')
plt.ylabel('Total Admissions')

plt.savefig('Graphs/Total Admissions Overlap Scatter 2.png')
plt.show()


















































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