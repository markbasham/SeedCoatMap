
from loaders import load_image_stack
from cubemap import build_cubemap_vector_array

from scipy.ndimage.filters import gaussian_filter
from scipy.ndimage.filters import median_filter, minimum_filter

from scipy.ndimage.measurements import center_of_mass

print('loading the data')
data = load_image_stack("/mnt/gpfs03/markb/87470/centered/recon*.tif",
                         slice(600, 1800),
                         slice(600, 1800),
                         slice(420, 1690))

print('filtering data')
data_filt = median_filter(data, 3)

print(' calculating center of mass, or a masks of everything above background')
com = center_of_mass(data_filt > 0.0001)

print('build the cubemap lookups')
x, y, z, r = build_cubemap_vector_array(com, mesh_size=200,
                                        min_radius=200,
                                        max_radius=800,
                                        radial_steps=1000)

print('Protect the limits')
x[x < 0] = 0
x[x >= data_filt.shape[0]] = data_filt.shape[0] - 1

y[y < 0] = 0
y[y >= data_filt.shape[1]] = data_filt.shape[1] - 1

z[z < 0] = 0
z[z >= data_filt.shape[2]] = data_filt.shape[2] - 1

print('generate the lookup data volume')
thick_vol = data_filt[x, y, z]

print('generate the thickness map')
thickmap = ((r-200)*(thick_vol<0.00015))
thickmap[thickmap==0] = 200
thickmap = thickmap.min(2)
thickmap[thickmap<0] = 0
dnp.plot.image(thickmap)

import matplotlib

matplotlib.image.imsave('/dls/tmp/ssg37927/thickmap.png', thickmap)

