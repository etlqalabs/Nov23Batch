import pandas as pd
df = pd.read_csv('TestData/emp.csv',delimiter='|')
# duplicated() function will return ‘True’ for all the rows which are duplicates
is_row_duplicates = df.duplicated()
print(df[is_row_duplicates])
