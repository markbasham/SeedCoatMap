'''
Created on 29 Mar 2019

@author: ssg37927
'''

from loaders import load_image_stack

from scipy.ndimage.filters import gaussian_filter
from scipy.ndimage.filters import median_filter, minimum_filter

from scipy.ndimage.measurements import center_of_mass


def main(template="/mnt/gpfs03/markb/87470/centered/recon*.tif",
         xslice=slice(600, 1800),
         yslice=slice(600, 1800),
         zslice=slice(420, 1690),
         background_threshold=0.0001):

    print('loading the data')
    data = load_image_stack(template, xslice, yslice, zslice)

    print('filtering data')
    data_filt = median_filter(data, 3)

    print(' calculating center of mass')
    com = center_of_mass(data_filt>background_threshold)

if __name__ == '__main__':
    print("Seems to be working")
    #main()
