# coding=utf-8
""" Module for fitting a sphere to a list of 3D points """

#let's use scipy's least squares optimisor
from scipy.optimize import leastsq
from math import sqrt
import numpy

def CalculateResidual(parameters, x, y , z):
    """ 
    Calculates the residual error for an x,y,z coordinates

    :return The residual error
    :param A tuple of the parameters to be optimised, should contain
    [x_centre, y_centre, z_centre, radius]
    :the x,y, and z coordinates.

    """
    
    #extract the parameters
    x_centre, y_centre, z_centre, radius = parameters
   
    print (x_centre, y_centre, z_centre, radius)

    #distance_from_centre = sqrt( (x-x_centre)**2 + (y-y_centre)**2 + (z-z_centre)**2 )
    distance_from_centre = numpy.sqrt((x-x_centre)**2 + (y-y_centre)**2 + (z-z_centre)**2) 
    error =  distance_from_centre - radius
    return error

def FitSphere_LeastSquares(x, y, z):
    """
    Uses scipy's least squares optimisor to fit a sphere to a set 
    of 3D Points
    
    :return The fitted sphere parameters, x, y, z, and radius and the residual error
    :param three lists of equal length containing the x, y, and z coordinates.
    """

    #initialise the parameters

    parameters=[0.0, 0.0, 0.0, 0.0]

    result = leastsq (CalculateResidual, parameters, args=(x,y,z))

    return result

from random import uniform
if __name__ == "__main__":
    x_centre = 1.0
    y_centre = 167.0
    z_centre = 200.0

    radius = 7.5
    
    xs=numpy.ndarray(shape=(1000,),dtype=float )
    ys=numpy.ndarray(shape=(1000,),dtype=float )
    zs=numpy.ndarray(shape=(1000,),dtype=float )
    #xs=numpy.zeros((1,10))
    #ys=numpy.zeros((1,10))
    #zs=numpy.zeros((1,10))
    for i in range(1000):
        #make a random vector
        x=uniform(-1.0, 1.0)
        y=uniform(-1.0, 1.0)
        z=uniform(-1.0, 1.0)
        
        #scale it to length radius
        length=sqrt( (x)**2 + (y)**2 + (z)**2 )
        factor = radius / length

        xs[i] = x*factor + x_centre
        ys[i] = y*factor + y_centre
        zs[i] = z*factor + z_centre

        
    
    result = FitSphere_LeastSquares(xs,ys,zs)
    print (result)



