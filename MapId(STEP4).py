import pandas as pd

# Load the CSV files, specifying the dtype for 'ea_id' to preserve leading zeros
df1 = pd.read_csv('ea_id.csv', dtype={'ea_id': str})  # Adjust the file name as needed
df2 = pd.read_csv('mergedCSV/merged_SPEI3_data.csv', dtype={'lat': float, 'lon': float})  # Adjust the file name as needed

# Round the latitude/longitude values in df2 to 2 decimal places for matching
df2['lat'] = df2['lat'].round(2)
df2['lon'] = df2['lon'].round(2)

# Create a function to round to the nearest value in a list
def round_to_nearest(val, round_vals):
    return round_vals.loc[(round_vals - val).abs().idxmin()]

# Drop rows with NaN values in ea_latitude and ea_longitude
df1 = df1.dropna(subset=['ea_latitude', 'ea_longitude'])

# Apply the rounding function to ea_latitude and ea_longitude, handling potential NaN values
df1['ea_latitude'] = df1['ea_latitude'].apply(lambda x: round_to_nearest(x, df2['lat']) if pd.notnull(x) else x)
df1['ea_longitude'] = df1['ea_longitude'].apply(lambda x: round_to_nearest(x, df2['lon']) if pd.notnull(x) else x)

# Merge the DataFrames based on the rounded latitude and longitude values
merged_df = pd.merge(df1, df2, left_on=['ea_latitude', 'ea_longitude'], right_on=['lat', 'lon'])

# Keep the necessary columns, including latitude, longitude, and time
final_df = merged_df[['ea_id', 'ea_latitude', 'ea_longitude', 'time', 'spei']]

# Save the resulting DataFrame to a new CSV file
final_df.to_csv('mapped_SPEI3.csv', index=False)

print(final_df)
