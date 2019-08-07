'''
Created on 29 Mar 2019

@author: ssg37927
'''

from numpy import meshgrid, linspace, concatenate, zeros_like, sqrt


def build_cubemap_vector_array(mesh_size=10):
    # create the tiles to build the x, y and z
    xt, yt = meshgrid(linspace(-1.0, 1.0, mesh_size),
                      linspace(-1.0, 1.0, mesh_size))
    zt = zeros_like(xt)
    ot = zt+1.0
    nt = zt-1.0

    xmap = concatenate(
        (concatenate((zt, xt, zt, zt), axis=1),
         concatenate((nt, xt, ot, xt[:, ::-1]), axis=1),
         concatenate((zt, xt, zt, zt), axis=1)))

    ymap = concatenate(
        (concatenate((zt, ot, zt, zt), axis=1),
         concatenate((yt[::-1, :], yt[::-1, :], yt[::-1, :], yt[::-1, :]), axis=1),
         concatenate((zt, nt, zt, zt), axis=1)))

    zmap = concatenate(
        (concatenate((zt, yt, zt, zt), axis=1),
         concatenate((xt, ot, xt[:, ::-1], nt), axis=1),
         concatenate((zt, yt[::-1, :], zt, zt), axis=1)))

    scale= sqrt(xmap**2+ymap**2+zmap**2)

    return (xmap/scale, ymap/scale, zmap/scale)