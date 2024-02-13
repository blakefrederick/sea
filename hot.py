import matplotlib.pyplot as plt
import numpy as np
from netCDF4 import Dataset
import cartopy.crs as ccrs
import cartopy.feature

# https://downloads.psl.noaa.gov/Datasets/COBE/
anomaly_file = 'sst.day.anom.2024.nc'

with Dataset(anomaly_file, mode='r') as anom_nc:
    # Extract the SST anomaly data and calculate the mean over time
    sst_anomaly = anom_nc.variables['anom'][:].mean(axis=0)

    lat = anom_nc.variables['lat'][:]
    lon = anom_nc.variables['lon'][:]
    
    # Magically generates a map
    fig = plt.figure(figsize=(15, 7))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.coastlines()
    cmap = plt.get_cmap('coolwarm')
    
    # Plot it
    anomaly_plot = ax.pcolormesh(lon, lat, sst_anomaly, cmap=cmap, transform=ccrs.PlateCarree())
    cbar = plt.colorbar(anomaly_plot, orientation='horizontal', pad=0.05, aspect=50)
    cbar.set_label('Sea Surface Temperature Anomaly (°C)')
    plt.title('Global Sea Surface Temperature Anomalies for 2024')
    plt.show()

    # Zoom in on (what appears to be) the most anomalous region
    zoomed_lat = 39.62
    zoomed_lon = 144.38
    lat_bounds = [34.62, 44.62]
    lon_bounds = [139.38, 149.38]

    # Zoomed in map
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.set_extent([lon_bounds[0], lon_bounds[1], lat_bounds[0], lat_bounds[1]], crs=ccrs.PlateCarree())
    ax.coastlines()
    ax.add_feature(cartopy.feature.LAND)
    ax.add_feature(cartopy.feature.OCEAN)
    anomaly_plot = ax.pcolormesh(lon, lat, sst_anomaly, cmap=cmap, transform=ccrs.PlateCarree())
    cbar = plt.colorbar(anomaly_plot, orientation='horizontal', pad=0.05, aspect=50)
    cbar.set_label('Sea Surface Temperature Anomaly (°C)')
    plt.title(f'Most Anomalous Region 39.62°, 144.38° (2024)')
    plt.show()
