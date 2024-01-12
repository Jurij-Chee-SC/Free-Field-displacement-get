import numpy as np
from scipy.interpolate import interp1d
import pandas as pd

data = pd.read_csv('y_matrix_498.csv')
# Extracting the depth and displacement values
depths = data['Z']
displacements = data.drop(columns=['Unnamed: 0', 'Z'])

# New depth values at 0.2 intervals
new_depths = np.arange(0, 16.8 + 0.2, 0.2)  # 16.8 is included, hence 0.2 is added

# Creating an interpolation function for each column (time step)
interpolated_data = pd.DataFrame()
interpolated_data['Z'] = new_depths

for col in displacements.columns:
    # Interpolation function for each time step
    f = interp1d(depths, displacements[col], kind='linear', fill_value="extrapolate")
    # Applying the interpolation function to the new depth values
    interpolated_data[col] = f(new_depths)
interpolated_data.to_csv('y_matrix02_498.csv')
print(interpolated_data)
