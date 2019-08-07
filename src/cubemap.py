'''
Created on 29 Mar 2019

@author: ssg37927
'''

from numpy import meshgrid, linspace, concatenate, zeros_like, sqrt, int16


def build_cubemap_vector_array(com, mesh_size=10,
                               min_radius=200,
                               max_radius=300,
                               radial_steps=10):
    # create the tiles to build the x, y and z
    xt, yt, rt= meshgrid(linspace(-1.0, 1.0, mesh_size),
                         linspace(-1.0, 1.0, mesh_size),
                         linspace(min_radius, max_radius, radial_steps))
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

    rmap = concatenate(
        (concatenate((zt, rt, zt, zt), axis=1),
         concatenate((rt, rt, rt, rt), axis=1),
         concatenate((zt, rt, zt, zt), axis=1)))

    scale = sqrt(xmap**2 + ymap**2 + zmap**2)

    return ((((xmap/scale)*rmap)+com[0]).astype(int16),
            (((ymap/scale)*rmap)+com[1]).astype(int16),
            (((zmap/scale)*rmap)+com[2]).astype(int16),
            rmap)
