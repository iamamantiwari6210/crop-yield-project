import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

import pickle

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
    
# load cleaned dataset
df = pd.read_csv("cleaned_crop_data.csv")

# feature and target
X = df[['Area']]
y = df['yield']

# train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# create model
model = RandomForestRegressor()

# train model
model.fit(X_train, y_train)

# prediction
predictions = model.predict(X_test)

# check error
error = mean_absolute_error(y_test, predictions)

print("Model Error:", error)

# show some predictions
print("Sample Predictions:")
print(predictions[:10])


import joblib
# save model
joblib.dump(model, "crop_yield_model.pkl")

print("Model saved successfully")