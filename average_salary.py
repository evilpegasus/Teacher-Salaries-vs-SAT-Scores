import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

#display 500 rows and 500 columns
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)





#Teacher salary data

df = pd.read_excel('WA_Secondary_Teachers_2018-2019.xlsx', index_col=0, usecols= [0, 2, 6])
df['Average Salary'] = df.groupby('School District')['Total Salary'].transform('mean')

print(df)

districts = df.groupby('School District', as_index=True).nunique()
districts['Average Salary'] = df.groupby('School District')['Total Salary'].mean()

print(districts)

#Number of rows (unique districts)
print("There are " + str(districts.shape[0]) + " districts")
print("Average of average secondary teacher salary by district is " + str(districts['Average Salary'].mean()))

#Copy averages to Excel
#districts.to_excel("average_salary.xlsx")

def get():
    return districts

