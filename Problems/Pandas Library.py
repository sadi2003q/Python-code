import pandas as pd
dict = {
    "name": ["Adnan ", "Abdullah", "Sadi", "Tamim", "Sufian", "Abu", "Mohammod"],
    "marks" : [87, 77, 82, 89, 88, 71, 93],
    "location": ["Dhaka", "Rajshahi", "Khulna", "Barishal", "Rangpur", "Singapore", "Arabia"],
    "cgpa" : [3.2, 3.4, 3.5, 3.1, 3.9, 3.6, 4.0]
}

df = pd.DataFrame(dict)
#df.to_csv('simple.csv', index= False)

df.head(2) # will show first 2 rows of the Dataset
df.tail(2) # will show first 2 rows of the Dataset
#print(df.describe()) # will describe the some analysis of numerical dataset

#print(pd.read_csv('simple.csv')) # read exel file

sadi = pd.read_csv('../Pandas/simple.csv')


print(sadi['name'][6]) # printing simple column ['row name'] printing specific value of the column ['column name'][row number]
sadi['location'][3] = 'Matuail' # will change the value of that column

print(sadi)


