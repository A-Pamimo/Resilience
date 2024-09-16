import xarray as xr
import os

# Load the NetCDF file
file_path = r'outputNcdf/spei06.nc'
ds = xr.open_dataset(file_path, engine='netcdf4')

# Specify the variable name (SPEI) you want to extract
SPEI_variable = 'spei'

# Define the time slice for 2020 onwards
time_slice = slice('2020-01-01', None)

# Filter the dataset for the specified time range
filtered_ds = ds[SPEI_variable].sel(time=time_slice)

# Create a new NetCDF file to save the filtered data
output_file_path = 'filteredSPEINc/SPEI06_filtered.nc'
filtered_ds.to_netcdf(output_file_path)

print(f"Filtered data from 2020 onwards has been saved to '{output_file_path}'")
