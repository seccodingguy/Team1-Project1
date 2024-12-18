# Team1-Project1
# Project Overview
This project focuses on performing **Exploratory Data Analysis (EDA)** on multiple datasets. The notebook includes functionality for loading, cleaning, analyzing, and visualizing data using Python libraries such as `pandas`, `matplotlib`, `seaborn`, and `numpy`. The reusable functions enable efficient handling of data cleaning, outlier detection, and correlation analysis.

The analysis is driven by the hypothesis: The overall Air Quality increased due to less commerce, driving, etc. during the onset of the COVID pandemic.

The data was sourced from the EPA Air Quality (https://www.epa.gov/air-quality) site to obtain monthly AQI data from 2019-2021 for the following three US cities, chosen with varying population levels:
<ul>
<li>Los Angeles, California (Pop. 3.8 Million)</li>
<li>St, Louis, Missouri (Pop 280,000)</li>
<li>Jeaneu, Alaska (Pop 31,500)</li>
</ul>

By sourcing cities with different population levels and geographical regions, we hope to get a more definitive picture of the data
from the analysis that answers the following:
<ul>
<li>How did the AQI change in each city from 2019-2021?</li>
<li>6 months before pandemic declaration (March 11th, 2020)</li>
<li>6 months during pandemic declaration</li>
<li>6-12 months after pandemic exploration</li>
</ul>

## Features
- **Load and Combine Data**: Reads multiple CSV files from a specified directory and combines them into a single DataFrame.
- **Data Cleaning**: Handles missing values, duplicates, and outliers.
- **Data Visualization**: Provides visualizations such as:
    - Boxplots for outlier detection
    - Heatmaps for correlation analysis
    - Pairplots for numerical data analysis
- **Data Slicing**: Slice data by city or date range for focused analysis.

## Installation
Before running the notebook, ensure that the required libraries are installed:

```bash
pip install pandas matplotlib seaborn numpy tqdm
```

## Usage
1. **Setup the Project**:
   - Place all relevant CSV files in a designated folder (e.g., `data/`).
   - Update the path in the notebook where required.

2. **Run the Notebook**:
   - Open the Jupyter Notebook.
   - Execute each cell sequentially to load, clean, and analyze the data.

3. **Functions Overview**:
   - `load_and_extract_data(path_to_csv)`: Combines all CSV files into a single DataFrame.
   - `clean_data(df)`: Cleans the data by handling missing values and duplicates.
   - `visualize_outliers(df, column)`: Displays boxplots to detect outliers.
   - `remove_outliers(df, column_name)`: Removes outliers based on the IQR method.
   - `visualize_data(df)`: Generates pairplots and correlation heatmaps.
   - `slice_by_city(city_name, city_column, df)`: Filters data for a specific city.
   - `slice_by_date(start_date, end_date, date_column, df)`: Slices data within a date range.

## Example Output
- **Combining Data**:
   ```text
   ['Juneau 2019 data.csv', 'Juneau 2020 data.csv', 'Los Angeles 2019 data.csv', ...]
   Loading data from CSV and combining to a single DataFrame: 100%|██████████| 11/11 [00:00<00:00, 30.82it/s]
   ```

- **Outlier Visualization**:
   ![Boxplot Example](example_boxplot.png)

- **Correlation Heatmap**:
   ![Heatmap Example](example_heatmap.png)

## Results Summary
The project enables users to:
1. Combine and analyze multiple datasets efficiently.
2. Identify and handle data quality issues such as missing values and outliers.
3. Generate insights using visualizations to understand relationships between variables.

## Directory Structure
```
project-root/
├── data/               # Folder for CSV files
├── Project 1.ipynb     # Jupyter Notebook
├── README.md           # This file
└── example_outputs/    # Folder for example images
```

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.

---
For questions or feedback, please reach out via GitHub Issues.

## Screenshots 

![LA Cleaned Data](screenshots/image-1.png)
![La Line Graph](screenshots/image-2.png)
![Juneau](screenshots/image-3.png)
![St Louis](screenshots/image-5.png)
![Juneau](screenshots/image-4.png)
![Juneau](screenshots/image-6.png)
![All three Cities](screenshots/image-7.png)