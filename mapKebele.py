import pandas as pd

# Load the 'mapped_SPEI1.csv' file into a DataFrame
df1 = pd.read_csv('mappedCSV/mapped_SPEI3.csv')

# Load the 'kebele.csv' file into a DataFrame
df2 = pd.read_csv('kebele.csv')

# Merge the DataFrames on the 'ea_id' column, adding the 'saq06' column from 'kebele.csv'
merged_df = pd.merge(df1, df2[['ea_id', 'saq06']], on='ea_id', how='left')

# Save the merged DataFrame to a new CSV file
merged_df.to_csv('kebele_mapped_SPEI3.csv', index=False)

print("New CSV file created with the 'saq06' column added.")
