import os
import pandas as pd

# Define the folder containing the CSV files
input_folder = r'C:\Users\olanrewaju\PycharmProjects\ResilienceStudy\spei3'
output_file = 'mergedCSV/merged_SPEI3_data.csv'

# Get a list of all CSV files in the folder
csv_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]

# Initialize an empty list to hold dataframes
dataframes = []

# Read each CSV file and append it to the list
for file in csv_files:
    file_path = os.path.join(input_folder, file)
    df = pd.read_csv(file_path)
    dataframes.append(df)

# Concatenate all dataframes in the list
merged_df = pd.concat(dataframes, ignore_index=True)

# Save the merged dataframe to a new CSV file
merged_df.to_csv(output_file, index=False)

print(f"All CSV files in the '{input_folder}' folder have been merged into '{output_file}'")
