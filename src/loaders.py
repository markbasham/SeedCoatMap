'''
Created on 29 Mar 2019

@author: ssg37927
'''
from numpy import dstack
from skimage import io
from h5py import File


def load_image_stack(template,
                     xslice=slice(None),
                     yslice=slice(None),
                     zslice=slice(None)):
    '''
    This method takes a sliced region from a stack of images and returns
    a single numpy array of all the data
    '''
    ims = io.imread_collection(template)
    count = 0
    stack = []
    for im in ims[zslice]:
        stack.append(im[xslice, yslice])
        print(count)
        count += 1
    return dstack(stack)


def save_data(filename, dataname, data):
    f = File(filename, 'w')
    f.create_dataset(dataname, data.shape, data.dtype, data)
    f.close()


def load_data(filename, dataname):
    f = File(filename, 'r')
    return f[dataname][...]
