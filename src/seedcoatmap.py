'''
Created on 29 Mar 2019

@author: ssg37927
'''

from loaders import load_image_stack
from cubemap import build_cubemap_vector_array

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

    print('build the cubemap lookups')
    xmap, ymap, zmap = build_cubemap_vector_array(com, mesh_size=10)




if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument("-t", "--template",
                        default="/mnt/gpfs03/markb/87470/centered/recon*.tif",
                        help="template which describes the tiff files for loading")
    parser.add_argument("--x_start", default=600)
    parser.add_argument("--x_stop", default=1800)
    parser.add_argument("--x_step", default=1)
    parser.add_argument("--y_start", default=600)
    parser.add_argument("--y_stop", default=1800)
    parser.add_argument("--y_step", default=1)
    parser.add_argument("--z_start", default=420)
    parser.add_argument("--z_stop", default=1690)
    parser.add_argument("--z_step", default=1)
    parser.add_argument("--background_threshold", default=0.0001,
                        help="Threshold below which is considered air")

    args = parser.parse_args()
    main(template=args.template,
         xslice=slice(args.x_start, args.x_stop, args.x_step),
         yslice=slice(args.x_start, args.x_stop, args.x_step),
         zslice=slice(args.x_start, args.x_stop, args.x_step),
         background_threshold=args.background_threshold)
