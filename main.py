import pandas as pd

df = pd.read_csv('sales.csv', header=0)


print('***My CVS File****'); print(df)

# ******reading column sales

print('******Reading Column Sales Only*****'); print(df['sales'])

#*********Collect all of the sales from each month into a single list

print('*****Collecting all of the sales from each month into a single list*****')
print(df['sales'].tolist())

print(df.values.tolist())

#          *********Sorting by column sales
print('****Sorted by column sales*****')
print(df.sort_values(by='sales'))

#        ***************Output the total sales across all months

A = df['sales'].sum()
B = df['expenditure'].sum()

print('*****Total of Sales****'); print(A)

#****************** Percentage of sales

percent_of_Sales = (B / A)*100

print('****Percent of Sales****'); print("%.0f%%" % percent_of_Sales)

#***********************************

print('********THE BIGGEST SALES***********'); print(df[df['sales']== df['sales'].max()])

#************* AVERAGE
#print('****Total Average****'); print(df.mean(axis='index'))


# ************ summary of statistics *********
print('*********summary of statistics******')
print(df.describe())
grouped_df = df.groupby(['month']).max()
print('*****Maximum Sales per Month*****')
print(grouped_df['sales'])

#***********************Grand total
print('******Grand Total******')
df[['sales', 'expenditure']].sum()
df.loc['Grand total'] = df[['sales', 'expenditure']].sum()
df.loc['Grand total'] = df.loc['Grand total'].fillna('')
print(df.loc['Grand total'])

print('*******************************************************')
print('********Use a data source from a different spreadsheet********')
data = pd.read_csv('trees.csv', header=0)
print('***My CVS Trees****'); print(data)

#*********Display the first 10 rows
result = data.head(10)
print("*********First 10 rows of the Trees*************:")
print(result)

grouped_data = data.groupby(['age']).max()
print('***** Trees by age *****')
print(grouped_data['species'])

#******** HIGHEST TREES***********

print('********THE YOUNGUEST TREES***********'); print(data[data['age']== data['age'].min()])


print('********THE HIGHEST TREES***********'); print(data[data['height']== data['height'].max()])


print('******************THE OLDEST TREES*************'); print(data[data['age']== data['age'].max()])


