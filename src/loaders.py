'''
Created on 29 Mar 2019

@author: ssg37927
'''
from numpy import dstack
from skimage import io


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
