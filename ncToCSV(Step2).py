import xarray as xr
import pandas as pd
import dask
import os
from dask.diagnostics import ProgressBar

# Load the NetCDF file with Dask
file_path = 'PDSI_cut_file.nc'
ds = xr.open_dataset(file_path, engine='netcdf4', chunks={'time': 'auto'})

# Specify the variable name (SPEI) you want to extract
SPEI_variable = 'PDSI'

# Filter the dataset for the specified latitude and longitude ranges
lat_range = slice(0, 15)
lon_range = slice(32, 48)
filtered_ds = ds[SPEI_variable].sel(lat=lat_range, lon=lon_range)

# Create a new folder called 'spei1' if it does not exist
output_folder = 'PDSI'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Define a function to process and save each month's data
def save_monthly_data(ds, output_folder):
    ds = ds.dropna(dim='time', how='all')
    times = pd.to_datetime(ds['time'].values)
    months = times.to_period('M')

    for month in pd.unique(months):
        # Check if the year is 2020 or later
        if month.year >= 2020:
            month_str = month.strftime('%Y-%m')
            output_file = os.path.join(output_folder, f'SPEI_data_{month_str}.csv')

            # Select data for the current month
            ds_month = ds.sel(time=times[months == month])

            # Convert to DataFrame
            df_month = ds_month.to_dataframe().reset_index()

            # Save to CSV
            df_month.to_csv(output_file, index=False)

# Process and save data month by month
with ProgressBar():
    save_monthly_data(filtered_ds, output_folder)

print("Non-NaN SPEI data from 2020 onwards has been saved to CSV files in the 'spei1' folder")
