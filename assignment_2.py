
#for the period 2071-2100
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import xarray as xr
dset = xr.open_dataset(r'C:\Users\mousabm\Downloads\Course_Data\Climate_Model_Data\tas_Amon_GFDL-ESM4_ssp119_r1i1p1f1_gr1_201501-210012.nc')
mean_2071_2100 = np.mean(dset['tas'].sel(time = slice('20710101','21001231')), axis=0)
mean_2071_2100 = np.array(mean_2071_2100)
pdb.set_trace()

#to get the figure I used the following code
plt.imshow(mean_2071_2100)
cbar = plt.colorbar()
cbar.set_label('Mean Air Temperature at 2071-2100 (K)')
plt.show()
plt.savefig('2071-2100.png', dpi=300)

#for the period 1850-1949
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import xarray as xr
dset = xr.open_dataset(r'C:\Users\mousabm\Downloads\Course_Data\Climate_Model_Data\tas_Amon_GFDL-ESM4_historical_r1i1p1f1_gr1_185001-194912.nc')
mean_1850_1900 = np.mean(dset['tas'].sel(time = slice('18500101','19001231')), axis=0)
mean_1850_1900 = np.array(mean_1850_1900)
pdb.set_trace()

#to get the figure I used the following code
plt.imshow(mean_1850_1900)
cbar = plt.colorbar()
cbar.set_label('Mean Air Temperature at 1850-1900 (K)')
plt.show()
plt.savefig('1850_1900.png', dpi=300)

#This code was wriiten after following the instructions in the assignment
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import xarray as xr
dset = xr.open_dataset(r'C:\Users\mousabm\Downloads\Course_Data\Climate_Model_Data\tas_Amon_GFDL-ESM4_historical_r1i1p1f1_gr1_195001-201412.nc')
pdb.set_trace()