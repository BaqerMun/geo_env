import xarray
dset = xarray.open_dataset(r'C:\Users\mousabm\Downloads\Course_Data\ERA5_Data\download.nc')
import numpy as np
t2m = np.array(dset.variables['t2m'])
tp = np.array(dset.variables['tp'])
latitude = np.array(dset.variables['latitude'])
longitude = np.array(dset.variables['longitude'])
time_dt = np.array(dset.variables['time'])

t2m = t2m - 273.15
tp = tp * 1000

if t2m.ndim == 4: t2m = np.nanmean(t2m, axis=1) ; tp = np.nanmean(tp, axis=1)

import pandas as pd
import matplotlib.pyplot as plt
df_era5 = pd.DataFrame(index=time_dt) 
df_era5['t2m'] = t2m
df_era5['tp'] = tp

df_era5.plot()
plt.show()


