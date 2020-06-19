import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

#find average salary of all secondary teachers in WA

#display 500 rows and 500 columns
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)





#Teacher salary data
df = pd.read_excel('WA_Secondary_Teachers_2018-2019.xlsx', index_col=0, usecols= [0, 2, 6])

print(df)
secondary_teacher_avg = df.mean(axis = 0)
print("Average salary of all secondary teachers = " + str(secondary_teacher_avg[0]))

def get():
    return secondary_teacher_avg[0]