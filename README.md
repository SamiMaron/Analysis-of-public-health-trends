# Analysis-of-public-health-trends 📊

## Project Overview 🎯
This project demonstrates my skills in data analysis, cleaning, and processing. The goal is to take raw data from a CSV file, clean it by handling missing values and ensuring proper data types, and finally save the cleaned dataset. The data used in this project contains information about various countries, their income per capita, and life expectancy.

## Key Tasks and Steps 🔑

1. **Load the Data** 📥:
   - I loaded the dataset from a CSV file and read it into a Pandas DataFrame using the `pd.read_csv()` function.

2. **Data Cleaning** 🧹:
   - I cleaned the dataset by:
     - Dropping rows with missing values using `dropna()`.
     - Converting columns like `income_per_capita` and `life_expectancy` to numeric types using `pd.to_numeric()` to ensure proper data formatting.

3. **Saving the Cleaned Data** 💾:
   - After cleaning the data, I saved the cleaned dataset as a new CSV file to the `outputs` folder using `to_csv()`.

## Technologies and Tools Used 🛠️

- **Python** 🐍: The core programming language used for data manipulation.
- **Pandas** 📚: A powerful data analysis library used for handling and cleaning the dataset.
- **OS** 🖥️: Used to check if the file exists before reading it.
- **CSV Files** 📄: The data format used for storing and processing the dataset.

