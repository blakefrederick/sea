import matplotlib.pyplot as plt
import numpy as np
from netCDF4 import Dataset
import cartopy.crs as ccrs
import cartopy.feature
import argparse

# https://downloads.psl.noaa.gov/Datasets/COBE/
anomaly_file = 'sst.day.anom.2024.nc'

# Let the user decide where to zoom to
parser = argparse.ArgumentParser()
parser.add_argument('lat_min', type=float)
parser.add_argument('lat_max', type=float)
parser.add_argument('lon_min', type=float)
parser.add_argument('lon_max', type=float)
args = parser.parse_args()

print(args.lat_min, args.lat_max, args.lon_min, args.lon_max)

with Dataset(anomaly_file, mode='r') as anom_nc:
    # Extract the SST anomaly data and calculate the mean over time
    sst_anomaly = anom_nc.variables['anom'][:].mean(axis=0)
    lat = anom_nc.variables['lat'][:]
    lon = anom_nc.variables['lon'][:]
    lat_bounds = [args.lat_min, args.lat_max]
    lon_bounds = [args.lon_min, args.lon_max]

    # map
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.set_extent([lon_bounds[0], lon_bounds[1], lat_bounds[0], lat_bounds[1]], crs=ccrs.PlateCarree())
    ax.coastlines()
    ax.add_feature(cartopy.feature.LAND)
    ax.add_feature(cartopy.feature.OCEAN)
    cmap = plt.get_cmap('coolwarm')
    anomaly_plot = ax.pcolormesh(lon, lat, sst_anomaly, cmap=cmap, transform=ccrs.PlateCarree())
    cbar = plt.colorbar(anomaly_plot, orientation='horizontal', pad=0.05, aspect=50)
    cbar.set_label('Sea Surface Temperature Anomaly (°C) (2024)')
    plt.title(f'Zoomed Region: Lat {lat_bounds[0]} to {lat_bounds[1]}, Lon {lon_bounds[0]} to {lon_bounds[1]}')
    plt.show()
