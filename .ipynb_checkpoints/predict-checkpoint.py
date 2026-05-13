import joblib

# load trained model
model = joblib.load("crop_yield_model.pkl")

# example input
area = [[100]]

# prediction
prediction = model.predict(area)

print("Predicted Yield:", prediction)