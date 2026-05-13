import pandas as pd
import sqlite3

# load cleaned dataset
df = pd.read_csv("cleaned_crop_data.csv")
print(df.columns)
# create database
conn = sqlite3.connect("agriculture.db")

# store dataset in SQL table
df.to_sql("crop_data", conn, if_exists="replace", index=False)

print("Data stored in SQL database successfully")

# example SQL query
query = """
SELECT State_Name, SUM(Production) as Total_Production
FROM crop_data
GROUP BY State_Name
ORDER BY Total_Production DESC
"""

result = pd.read_sql(query, conn)

print(result.head())