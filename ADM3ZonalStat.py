# import necessary packages
import xarray as xr
import rasterio as rio
import geopandas as gpd
import rasterstats as rstats
import pandas as pd

# Load and read the shapefile (.shp file) with geopandas
shp_fo = r'eth_adm_csa_bofedb_2021_shp/eth_admbnda_adm3_csa_bofedb_2021.shp'
shp_df = gpd.read_file(shp_fo)

# Check if ADM3_PCODE is present in the attributes and confirm the count
if 'ADM3_PCODE' in shp_df.columns:
    gid3_codes = shp_df['ADM3_PCODE'].unique()
    print(f"Number of unique ADM3_PCODEs: {len(gid3_codes)}")
    assert len(gid3_codes) == 1082, "The number of ADM3_PCODEs is not 1082!"
else:
    raise KeyError("ADM3_PCODE field is not found in the shapefile.")

# Load and read netCDF-file to dataset and get datarray for variable
nc_fo = r'filteredSPEINc/SPEI06_filtered.nc'
nc_ds = xr.open_dataset(nc_fo)
nc_var = nc_ds['spei']

# Get affine of nc-file with rasterio
affine = rio.open(nc_fo).transform

# Initialize a list to store results
zonal_stats_results = []

# Get all years for which we have data in nc-file
years = nc_ds['time'].values

# Go through all years
for year in years:
    # Get values of variable per year
    nc_arr = nc_var.sel(time=year)
    nc_arr_vals = nc_arr.values

    # Go through all geometries and compute zonal statistics
    for i in range(len(shp_df)):
        stats = rstats.zonal_stats(
            shp_df.geometry[i], nc_arr_vals, affine=affine, stats="mean min max"
        )
        stats[0]['year'] = str(year)  # Add the year to the result
        stats[0]['adm3_pcode'] = shp_df['ADM3_PCODE'].iloc[i]  # Use ADM3_PCODE as the unique identifier
        zonal_stats_results.append(stats[0])

# Convert the list of results into a DataFrame
df = pd.DataFrame(zonal_stats_results)

# Save the DataFrame to a CSV file
df.to_csv('zonal_stats_SPEI6.csv', index=False)

print("Zonal statistics saved to 'zonal_stats_results.csv'")
