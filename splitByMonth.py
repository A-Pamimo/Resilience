import os
import pandas as pd

# Path to the input CSV file
input_csv = r'C:\Users\olanrewaju\PycharmProjects\ResilienceStudy\mappedCSV\mapped_SPEI1.csv'

# Directory to save the monthly CSV files
output_dir = 'spei1_monthly_data'
os.makedirs(output_dir, exist_ok=True)

# Load the CSV file
df = pd.read_csv(input_csv)

# Convert the 'time' column to datetime format
df['time'] = pd.to_datetime(df['time'])

# Extract year and month for grouping
df['year_month'] = df['time'].dt.to_period('M')

# Group by year and month, and save each group to a separate CSV file
for period, group in df.groupby('year_month'):
    # Format the period to 'YYYY-MM' for the filename
    period_str = period.strftime('%Y-%m')
    output_file = os.path.join(output_dir, f'{period_str}.csv')
    group.drop(columns='year_month').to_csv(output_file, index=False)  # Drop 'year_month' column before saving

print(f"Monthly CSV files saved in directory: {output_dir}")
