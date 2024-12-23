import pandas as pd

#Load "Dataset.csv" into df
#Dataset uses ";" as a delimiter and it's a huge file so low_memory = False to avoid chunk loading
df = pd.read_csv('Dataset.csv', sep = ";", low_memory = False)

#EDA:

#Display the first 5 rows
print("Original Dataset:")
print(df.head())
print("---------------------------------")

#Show Column names
print("Column labels:")
print(df.info())