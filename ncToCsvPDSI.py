import xarray as xr
import os

# Load the NetCDF file
nc_file = 'PDSI_cut_file.nc'
ds = xr.open_dataset(nc_file)

# Create a directory named 'PDSI' if it doesn't exist
output_dir = 'PDSI'
os.makedirs(output_dir, exist_ok=True)

# Convert to DataFrame in chunks
chunk_size = 1000  # Adjust the chunk size as needed

# Iterate over chunks and save each to a separate CSV file
for i in range(0, len(ds['time']), chunk_size):
    chunk = ds.isel(time=slice(i, i + chunk_size)).to_dataframe().reset_index()
    chunk_file = os.path.join(output_dir, f'chunk_{i//chunk_size}.csv')
    chunk.to_csv(chunk_file, index=False)

print(f"Chunks saved in directory: {output_dir}")
