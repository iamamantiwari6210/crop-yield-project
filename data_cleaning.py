import pandas as pd

# load dataset
df = pd.read_csv("crop_production.csv")

# remove missing values
df = df.dropna()

# remove area = 0
df = df[df["Area"] != 0]

# create new column
df["yield"] = df["Production"] / df["Area"]

# save cleaned dataset
df.to_csv("cleaned_crop_data.csv", index=False)

print("Data cleaned successfully")