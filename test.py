import pandas as pd

df = pd.ExcelFile('DIJ - 01.2022.xlsx')
print(df.sheet_names)
df1 = df.parse('Pool')
print(df1)


# drop everything except rows 2, 4, and 45/46
df2 = df1.iloc[[2, 4, 45, 46]]
print(df2)
