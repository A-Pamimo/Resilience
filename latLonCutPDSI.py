import xarray as xr

# Open the NetCDF file
nc_file = 'PDSI_merged.nc'
ds = xr.open_dataset(nc_file)

# Print the dataset to inspect its structure
print(ds)

# Define the latitude and longitude ranges
# Here we select approximate ranges that are more likely to match the dataset
lat_min, lat_max = 0, 15
lon_min, lon_max = 32, 48

# Find the closest available coordinates within the specified range
lat_range = ds['lat'].where((ds['lat'] >= lat_min) & (ds['lat'] <= lat_max), drop=True)
lon_range = ds['lon'].where((ds['lon'] >= lon_min) & (ds['lon'] <= lon_max), drop=True)

# Check if the ranges are empty
if lat_range.size == 0 or lon_range.size == 0:
    print("The specified ranges do not match any available data points.")
else:
    # Cut the dataset along the specified latitude and longitude ranges
    ds_cut = ds.sel(lat=lat_range, lon=lon_range)

    # Save the cut dataset to a new NetCDF file
    output_file = 'PDSI_cut_file.nc'
    ds_cut.to_netcdf(output_file)
    print(f"The dataset has been cut and saved to {output_file}")
