import pandas as pd

df = pd.ExcelFile('DIJ - 01.2022.xlsx')
print(df.sheet_names)
df1 = df.parse('Pool')
print(df1)


# drop everything except needed rows
df2 = df1.iloc[[46,47]]
print(df2)

# now we add the two rows together
df3 = df2.iloc[0] + df2.iloc[1]
print(df3)
