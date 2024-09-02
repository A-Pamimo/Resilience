import os
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import Point

# Set the folder path for your data files
folder_path = r'spei1_monthly_data'

# Set the path for the Ethiopia shapefile
shape_file = r'C:\Users\olanrewaju\PycharmProjects\ResilienceStudy\gadm41_ETH_shp\gadm41_ETH_3.shp'

# Create the output directory for images if it doesn't exist
output_dir = 'spei1_monthly_images_v2'
os.makedirs(output_dir, exist_ok=True)

# Loop through all .csv files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)  # Read CSV file

        # Convert the DataFrame to a GeoDataFrame
        geometry = [Point(xy) for xy in zip(df.ea_longitude, df.ea_latitude)]
        gdf = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")

        # Load Ethiopia shapefile
        ethiopia = gpd.read_file(shape_file)

        # Create the plot
        fig, ax = plt.subplots(figsize=(15, 10))

        # Plot Ethiopia
        ethiopia.plot(ax=ax, color='lightgrey', edgecolor='black')

        # Plot heat map using hexbin
        hb = ax.hexbin(gdf.geometry.x, gdf.geometry.y, C=gdf.spei, gridsize=50, cmap='RdYlBu', reduce_C_function=np.mean)

        # Customize the plot
        plt.title(f'SPEI Heat Map in Ethiopia - {filename}')
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        cbar = plt.colorbar(hb)
        cbar.set_label('Mean SPEI')

        # Adjust the plot extent to match Ethiopia's boundaries
        ax.set_xlim(ethiopia.total_bounds[0], ethiopia.total_bounds[2])
        ax.set_ylim(ethiopia.total_bounds[1], ethiopia.total_bounds[3])

        # Save the plot as an image
        image_file = os.path.join(output_dir, f'{os.path.splitext(filename)[0]}.png')
        plt.savefig(image_file, dpi=300)
        plt.close()

print(f"Images saved in directory: {output_dir}")
