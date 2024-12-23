import pandas as pd

#Load "Dataset.csv" into df
#Dataset uses ";" as a delimiter, and it's a huge file so low_memory = False to avoid chunk loading
df = pd.read_csv('Dataset.csv', sep = ";", low_memory = False)

#EDA:

#Display the first 5 rows
print("Original Dataset:")
print(df.head())
print("---------------------------------")

#Show Column names
print("Column labels:")
df.info()
print("--------------")

#Inspect if we have missing values or duplicate rows
print("#Missing Values: ", df.isnull().sum())
print("#Duplicate rows: ", df.duplicated().sum())
print("-----------------")

#Data Cleaning:

#Remove duplicate rows and the ones with missing values and make the index linearly consistent with the number of rows
df_cleaned = df.dropna(axis = 0, how = 'any')
df_cleaned = df_cleaned.drop_duplicates()
df_cleaned.reset_index(drop = True, inplace = True)
df_cleaned.info()
print("---------------------")
