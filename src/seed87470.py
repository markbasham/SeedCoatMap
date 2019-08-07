
from loaders import load_image_stack
from cubemap import build_cubemap_vector_array

from scipy.ndimage.filters import gaussian_filter
from scipy.ndimage.filters import median_filter, minimum_filter, maximum_filter

from scipy.ndimage.measurements import center_of_mass

import h5py
import numpy as np

with h5py.File('C:/data/87470/output.h5', 'w') as out_file:
    
    print('loading the data')
    data = load_image_stack("C:/data/87470/centered/recon*.tif",
                             slice(600, 1800, 2),
                             slice(600, 1800, 2),
                             slice(420, 1690, 2))
    
    print('filtering data')
    data_filt = median_filter(data, 3)
    
    out_file.create_dataset("data_filt", shape=data_filt.shape, dtype=data_filt.dtype, data=data_filt)
    
    print(' calculating center of mass, or a masks of everything above background')
    com = center_of_mass(data_filt > 0.0001)
    
    print('build the cubemap lookups')
    x, y, z, r = build_cubemap_vector_array(com, mesh_size=400,
                                            min_radius=000,
                                            max_radius=350,
                                            radial_steps=400)
    
    print('Protect the limits')
    x[x < 0] = 0
    x[x >= data_filt.shape[0]] = data_filt.shape[0] - 1
    
    y[y < 0] = 0
    y[y >= data_filt.shape[1]] = data_filt.shape[1] - 1
    
    z[z < 0] = 0
    z[z >= data_filt.shape[2]] = data_filt.shape[2] - 1
    
    print('generate the lookup data volume')
    thick_vol = data_filt[x.astype(np.int16), y.astype(np.int16), z.astype(np.int16)]
    
    out_file.create_dataset("thick_vol", shape=thick_vol.shape, dtype=thick_vol.dtype, data=thick_vol)
    
    print('generate the surface map')
    surface_map = (r*(thick_vol > 0.00015)).max(2)
    
    xt, yt, rt = np.meshgrid(range(surface_map.shape[1]),
                             range(surface_map.shape[0]),
                             range(50))
    
    a = []
    for i in range(50):
        a.append(surface_map.astype(np.int16)-rt[:,:,i])
    
    zlookup = np.dstack(a)
    zlookup[zlookup > 399] = 399
    
    remap_vol = thick_vol[yt,xt,zlookup]
    
    out_file.create_dataset("remap_vol", shape=remap_vol.shape, dtype=remap_vol.dtype, data=remap_vol)
    
    aa = ((remap_vol<0.00015)*rt)
    aa[aa==0] = 50
    
    out_file.create_dataset("aa", shape=aa.shape, dtype=aa.dtype, data=aa)
    
    thick_map = aa.min(2).astype(np.float32)
    thick_map[thick_map<1.5] = np.NaN
    from skimage.filters import threshold_local
    from skimage.morphology import dilation
    
    print("Work on creating a surface mask")
    
    filt_surf_map = median_filter(surface_map, 3)
    
    from astropy.convolution import Gaussian2DKernel, convolve
    
    smoothed_surf = convolve(np.pad(surface_map, 50, 'edge'), Gaussian2DKernel(50.0, x_size=101, y_size=101))[50:-50,50:-50]
    
    crack_map = (filt_surf_map-smoothed_surf)<-5
    
    coat_mask = crack_map==False
    
    coat_thick = coat_mask*thick_map
    coat_thick[coat_thick<=0] = np.NaN 
    
    
    np.nanmean(coat_thick)
    np.nanmax(coat_thick)
    np.nanmin(coat_thick)
    np.nanstd(coat_thick)
    
    print('All done')




