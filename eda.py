# Importing necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
from tqdm import tqdm


def load_and_extract_data(path_to_csv):
    # List all files in the directory and filter for CSV files
    csv_files = [file for file in os.listdir(path_to_csv) if file.endswith('.csv')]
    print(csv_files)
    count = len(csv_files)

    try:
        combined = pd.read_csv(os.path.join(path_to_csv,csv_files[0]))
        combined.reset_index()
        for i in tqdm(range(1,count),desc="Loading data from CSV and combining to a single DataFrame"):
            temp_df = pd.read_csv(os.path.join(path_to_csv,csv_files[i]))
            temp_df.reset_index()
            combined = pd.concat([combined,temp_df],axis=0)
    except Exception as e:
        print(f"{e}")

    return combined

def clean_data(df):
    """
    Clean the data: handle missing values and duplicates.
    """
    print("\n--- Cleaning Data ---")
    
    # Drop duplicate rows
    initial_shape = df.shape
    df = df.drop_duplicates()
    print(f"Removed duplicates: {initial_shape[0] - df.shape[0]} rows dropped.")
    
    # Fill missing numeric columns with median
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        df[col].fillna(df[col].median(), inplace=True)
    
    # Fill missing categorical columns with mode
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        df[col].fillna(df[col].mode()[0], inplace=True)

    print("Missing values handled.")
    return df

def visualize_outliers(df, y_value_column):
    # Boxplot
    sns.boxplot(data=df, y=y_value_column)
    plt.title("Boxplot for Outlier Detection")
    plt.show()

def remove_outliers(df, column_name):
    # Calculate Q1 (25th percentile) and Q3 (75th percentile)
    Q1 = df[column_name].quantile(0.25)
    Q3 = df[column_name].quantile(0.75)
    IQR = Q3 - Q1

    # Define the lower and upper bounds
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Find outliers
    outliers = df[(df[column_name] < lower_bound) | (df[column_name] > upper_bound)]

    print("Outliers:")
    print(outliers)

    # Remove outliers
    df_cleaned = df[(df[column_name] >= lower_bound) & (df[column_name] <= upper_bound)]

    return df_cleaned

def visualize_data(df):
    """
    Visualize the data: distributions and correlations.
    """
    print("\n--- Visualizing Data ---")
    plt.figure(figsize=(10, 6))
    
    # Pairplot for numerical columns
    print("Generating pairplot...")
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) > 1:
        sns.pairplot(df[numeric_cols])
        plt.show()
    
    # Heatmap for correlation
    print("Generating heatmap...")
    correlation_matrix = df.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title("Correlation Matrix Heatmap")
    plt.show()

def slice_by_city(city_name, city_column_name, data_frame):
    sliced_df = data_frame[data_frame[city_column_name] == city_name]
    return sliced_df

def slice_by_date(start_date, end_date, date_column_name, data_frame):
    data_frame.set_index(date_column_name)
    sliced_df = data_frame[(data_frame.index >= start_date) & (data_frame.index <= end_date)]
    sliced_df.reset_index()
    return sliced_df

def print_and_plot_corr_matrix(data_frame,columns):
    correlation_matrix = data_frame[columns].corr()
    print(correlation_matrix)
    # Plot the correlation matrix as a heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title("Correlation Matrix Heatmap")
    plt.show()
    

# Load the CSV file into a Pandas DataFrame
# Replace 'data.csv' with the path to your CSV file
#file_path = r"data/Los Angeles 2019 data.csv"
#df = pd.read_csv(file_path)
df = load_and_extract_data("data")
df = df[['Date', 'CBSA Name','Local Site Name', 'Daily AQI Value', 'Daily Mean PM2.5 Concentration']].copy()
df['Date'] = pd.to_datetime(df['Date'])

df = clean_data(df)
visualize_outliers(df,'Daily AQI Value')
visualize_outliers(df,'Daily Mean PM2.5 Concentration')

# Display the first few rows of the dataset
print("First 5 rows of the dataset:")
print(df.head())

# Display basic information about the dataset
print("\nDataset Information:")
df.info()

# Display basic statistics for numeric columns
print("\nDescriptive Statistics:")
print(df.describe())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check for duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# View the shape of the dataset
print("\nShape of the dataset:")
print(df.shape)

# Column-wise data types
print("\nColumn-wise Data Types:")
print(df.dtypes)

# Display unique values for categorical columns
print("\nUnique Values for Categorical Columns:")
categorical_columns = df.select_dtypes(include=['object']).columns
for col in categorical_columns:
    print(f"{col}: {df[col].unique()}")

matrix_names = ['Date','Daily AQI Value', 'Daily Mean PM2.5 Concentration']

# Check for correlations between numerical columns using Numpy
print("\nCorrelation Matrix:")
print_and_plot_corr_matrix(df,matrix_names)
#correlation_matrix = df[['Date','Daily AQI Value', 'Daily Mean PM2.5 Concentration']].corr()
#print(correlation_matrix)

city_names = ["Los Angeles-Long Beach-Anaheim, CA","Tallahassee, FL","Juneau, AK","St. Louis, MO-IL"]
city_column = "CBSA Name"

for city_name in city_names:
    df_slice = slice_by_city(city_name,city_column, df)
    print(f"\nCorrelation Matrix for {city_name}:")
    print_and_plot_corr_matrix(df_slice,matrix_names)
    #correlation_matrix = df_slice[['Date','Daily AQI Value', 'Daily Mean PM2.5 Concentration']].corr()
    #print(correlation_matrix)

# Check for outliers using interquartile range (IQR)
print("\nChecking for outliers:")
for column in df.select_dtypes(include=[np.number]).columns:
    Q1 = df[column].quantile(0.25)  # First quartile
    Q3 = df[column].quantile(0.75)  # Third quartile
    IQR = Q3 - Q1                   # Interquartile range
    outliers = df[(df[column] < (Q1 - 1.5 * IQR)) | (df[column] > (Q3 + 1.5 * IQR))]
    print(f"{column}: {len(outliers)} outliers")

# Visualize missing values (optional visualization using heatmap)
try:
    import seaborn as sns
    import matplotlib.pyplot as plt

    sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
    plt.title("Heatmap of Missing Values")
    plt.show()
except ImportError:
    print("\nSeaborn or Matplotlib not installed. Skipping visualization.")

# Summary of the EDA
print("\nEDA Summary Complete!")