# 🌾 Crop Yield Prediction Project

A machine learning-based system for predicting crop yield based on agricultural data. This project includes data cleaning, model training, database management, and an interactive web dashboard for real-time predictions.

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [Data Pipeline](#data-pipeline)
- [Model Details](#model-details)
- [Files Description](#files-description)

## 📖 Project Overview

This project aims to predict crop yield by analyzing agricultural parameters such as rainfall, temperature, humidity, and land area. It processes raw crop production data, trains a machine learning model, and provides an interactive dashboard for making predictions.

## ✨ Features

- **Data Cleaning**: Automatically preprocesses raw agricultural data, handles missing values, and calculates yield metrics
- **Machine Learning Model**: Random Forest Regressor trained on historical crop data
- **Database Integration**: SQLite database for storing and querying agricultural data
- **Interactive Dashboard**: Streamlit web application for real-time crop yield predictions
- **Data Analysis**: Jupyter notebooks for exploratory data analysis
- **Prediction API**: Python scripts for batch predictions

## 🛠️ Tech Stack

- **Python 3.x**
- **Pandas**: Data manipulation and analysis
- **Scikit-learn**: Machine learning model
- **SQLite**: Database management
- **Streamlit**: Web dashboard
- **Jupyter Notebook**: Data exploration and analysis
- **JobLib**: Model serialization
- **NumPy**: Numerical computations

## 📁 Project Structure

```
crop-yield-project/
├── app.py                      # Streamlit dashboard application
├── ml_model.py                 # ML model training and saving
├── data_cleaning.py            # Data preprocessing pipeline
├── database.py                 # Database setup and queries
├── predict.py                  # Prediction script
├── create_table.sql            # Database schema definition
├── crop_production.csv         # Raw crop production data
├── cleaned_crop_data.csv       # Processed crop data
├── data_analysis.ipynb         # Exploratory data analysis
├── crop_yield_model.pkl        # Trained ML model
├── agriculture.db              # SQLite database
└── README.md                   # Project documentation
```

## 🚀 Setup & Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Installation Steps

1. **Clone/Download the project**
   ```bash
   cd crop-yield-project
   ```

2. **Install required packages**
   ```bash
   pip install pandas scikit-learn streamlit joblib jupyter numpy
   ```

3. **Run data cleaning**
   ```bash
   python data_cleaning.py
   ```
   This will generate `cleaned_crop_data.csv` from the raw data.

4. **Train the ML model**
   ```bash
   python ml_model.py
   ```
   This creates `crop_yield_model.pkl` - the trained model.

5. **Set up the database**
   ```bash
   python database.py
   ```
   This creates `agriculture.db` and populates it with crop data.

## 💻 Usage

### Running the Web Dashboard
```bash
streamlit run app.py
```
The dashboard will open at `http://localhost:8501` where you can:
- Adjust rainfall, temperature, and humidity sliders
- View predicted crop yield
- Analyze crop-yield relationships through visualizations

### Making Predictions
```bash
python predict.py
```
This loads the trained model and demonstrates predictions on sample data.

### Data Analysis
Open and run the Jupyter notebooks:
```bash
jupyter notebook data_analysis.ipynb
```

## 📊 Data Pipeline

1. **Data Source**: `crop_production.csv` contains raw agricultural data
2. **Cleaning** (`data_cleaning.py`):
   - Removes missing values
   - Filters invalid data (Area ≠ 0)
   - Calculates yield = Production / Area
   - Outputs: `cleaned_crop_data.csv`
3. **Model Training** (`ml_model.py`):
   - Loads cleaned data
   - Splits into training (80%) and testing (20%)
   - Trains Random Forest Regressor
   - Evaluates with Mean Absolute Error
   - Saves model: `crop_yield_model.pkl`
4. **Database** (`database.py`):
   - Stores cleaned data in SQLite
   - Enables SQL queries for analytics
5. **Prediction** (`predict.py`):
   - Loads trained model
   - Makes predictions on new data

## 🤖 Model Details

- **Algorithm**: Random Forest Regressor
- **Features**: Area (land area in units)
- **Target**: Yield (production per unit area)
- **Train-Test Split**: 80-20
- **Evaluation Metric**: Mean Absolute Error (MAE)

The model can be extended to include additional features like rainfall, temperature, humidity, and crop type for improved accuracy.

## 📄 Files Description

| File | Purpose |
|------|---------|
| `app.py` | Streamlit web application with interactive dashboard |
| `ml_model.py` | Model training, evaluation, and saving |
| `data_cleaning.py` | Data preprocessing and cleaning |
| `database.py` | Database operations and SQL queries |
| `predict.py` | Batch prediction using trained model |
| `data_analysis.ipynb` | EDA and data visualization |
| `crop_production.csv` | Raw input data |
| `cleaned_crop_data.csv` | Processed data after cleaning |
| `create_table.sql` | SQL schema (currently unused) |

## 📝 Notes

- Ensure `crop_production.csv` exists before running `data_cleaning.py`
- Model training must be completed before running predictions
- Database setup recommended for scalable data management
- Dashboard provides visual insights into yield predictions

## 🔄 Future Enhancements

- Add more features (rainfall, temperature, humidity, soil type)
- Implement hyperparameter tuning
- Add data validation and error handling
- Deploy to cloud platform
- Create REST API for predictions
- Add seasonal analysis
- Implement real-time data ingestion
