import pandas as pd

# Load the merged CSV file into a DataFrame
merged_df = pd.read_csv('kebele_mapped_SPEI1.csv')

# Group by 'saq06' and calculate the mean of 'spei'
zonal_stats = merged_df.groupby('saq06')['spei'].mean().reset_index()

# Save the result to a new CSV file
zonal_stats.to_csv('zonal_statistics_SPEI1.csv', index=False)

print("Zonal statistics (mean of spei) calculated for unique saq06 values and saved to 'zonal_statistics.csv'.")
