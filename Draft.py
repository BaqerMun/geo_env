dset = xr.open_dataset(r'C:\Users\mousabm\Downloads\Gridsat\GRIDSAT-B1.2009.11.25.06.v02r01.nc')
IR = np.array(dset.variables['irwin_cdr']).squeeze()
IR.shape
IR = np.flipud(IR)
IR = IR*0.01+200
IR = IR-273.15
import matplotlib.pyplot as plt
plt.figure(1)
plt.imshow(IR, extent=[-180.035, 180.035, -70.035, 70.035], aspect='auto')
cbar = plt.colorbar()
cbar.set_label('Brightness temperature (degrees Celsius)')
jeddah_lat = 21.5
jeddah_lon = 39.2
plt.scatter(jeddah_lon, jeddah_lat, color='red', marker='o', label='Jeddah')