import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import average_salary
import sat

#get and print sat and salary dataframes from sat.py and average_salary.py respectively
sat_df = sat.get()
salary_df = average_salary.get()
print(sat_df)
print(salary_df)

#combine sat and salary dataframes into a combined dataframe
#take only the sat and average salary columns
combined_df = pd.concat([sat_df, salary_df], axis=1, sort=True)[['Total Score Mean', 'Average Salary']]
#remove rows with empty (NaN) values
combined_df = combined_df.dropna(axis = 0) #uncomment to fix pairing issues when district names don't match up

print(combined_df)
print("Combined dataframe has " + str(combined_df.shape[0]) + " data points")

#copy combined dataframe to Excel
#combined_df.to_excel("combined.xlsx")

#linear regression
X = combined_df['Average Salary'].values.reshape(-1, 1)
Y = combined_df['Total Score Mean'].values.reshape(-1, 1)
linear_regressor = LinearRegression()
linear_regressor.fit(X, Y)
Y_pred = linear_regressor.predict(X)

print("Coefficients: " + str(linear_regressor.coef_))
print("Y-int: " + str(linear_regressor.intercept_))
print("R^2: " + str(linear_regressor.score(X, Y)))

#plot data
ax = combined_df.plot.scatter(x='Average Salary', y='Total Score Mean')
ax.set_xlim(xmin = 0)
ax.set_ylim(bottom = 0)
plt.title('Mean SAT Scores vs. Mean Salaries')
plt.ylabel('Mean SAT Score')
plt.xlabel('Average Secondary Teacher Salary')

#plot regression line
plt.plot(X, Y_pred, color='red')

plt.show()