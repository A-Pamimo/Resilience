import pandas as pd

# Step 1: Read the CSV data into a pandas DataFrame
df = pd.read_csv('kebele_mapped_SPEI3.csv')

# Step 2: Convert the 'time' column to datetime and extract the year and month
df['time'] = pd.to_datetime(df['time'])
df['year'] = df['time'].dt.year
df['month'] = df['time'].dt.month

# Step 3: Group by 'saq06', 'year', and 'month', and calculate the mean SPEI
mean_spei_by_saq06_year_month = df.groupby(['saq06', 'year', 'month'])['spei'].mean().reset_index()

# Step 4: Save the result to a new CSV file
output_file_path = 'zonal_statistics_SPEI3.csv'
mean_spei_by_saq06_year_month.to_csv(output_file_path, index=False)

# Display a confirmation message
print(f"Results have been saved to {output_file_path}")


# Save the result to a new CSV file
print("Zonal statistics (mean of spei) calculated for unique saq06 values and saved to 'zonal_statistics.csv'.")
