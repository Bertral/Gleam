# nécessite environ 10 Go de RAM disponible, peut prendre jusqu'à 1h

import rasterio
import matplotlib.pyplot as plt
import numpy as np


valuesX = []
valuesY = []
valuesZ = []

raster = rasterio.open('../../Data/lightpop_merged/2000.tif')
valuesX = raster.read(1) # first band
valuesY = raster.read(2)

# normalize Z
#valuesZ = np.array(valuesZ).astype(np.float)
#valuesZ = (valuesZ - np.amin(valuesZ)) / (np.amax(valuesZ) - np.amin(valuesZ))
    
fig = plt.figure()
ax1 = plt.subplot(1, 1, 1)

#plt.xscale('log')
#plt.yscale('log')
ax1.scatter(valuesX, valuesY, alpha=0.01)
ax1.set(xlabel='?', ylabel='?')
ax1.grid()

fig.savefig("scatters/2000.png")

plt.close(fig)

print('plots done !')