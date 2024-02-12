from netCDF4 import Dataset

# So here we inspect the whathaveyous of the nc file (that I found here: https://downloads.psl.noaa.gov/Datasets/COBE/) so that a script can be written about it (hot.py)
nc_file = 'sst.day.anom.2024.nc'

def inspect_nc_file(file_path):
    # Open up the NetCDF file
    with Dataset(file_path, mode='r') as nc:
        print(f"Inspecting {file_path}")
        print("Dimensions:")
        for name, dimension in nc.dimensions.items():
            print(f" - {name}, length: {len(dimension)}")
        
        print("\nVariables:")
        for name, variable in nc.variables.items():
            print(f" - {name}, shape: {variable.shape}, data type: {variable.dtype}")

inspect_nc_file(nc_file)
