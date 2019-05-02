# coding=utf-8
""" Module for fitting a sphere to a list of 3D points """

#scipy has a nice least squares optimisor
from scipy.optimize import leastsq
import numpy

def fit_sphere_least_squares(x_values, y_values, z_values, initial_parameters):
    """
    Uses scipy's least squares optimisor to fit a sphere to a set
    of 3D Points

    :return: x: an array containing the four fitted parameters
    :return: ier: int An integer flag. If it is equal to 1, 2, 3 or 4, the
             solution was found.
    :param: (x,y,z) three arrays of equal length containing the x, y, and z
            coordinates.
    :param: an array containing four initial values (centre, and radius)
    """
    return leastsq(_calculate_residual_sphere, initial_parameters,
                   args=(x_values, y_values, z_values))

def _calculate_residual_sphere(parameters, x_values, y_values, z_values):
    """
    Calculates the residual error for an x,y,z coordinates, fitted
    to a sphere with centre and radius defined by the parameters tuple

    :return: The residual error
    :param: A tuple of the parameters to be optimised, should contain
            [x_centre, y_centre, z_centre, radius]
    :param: arrays containing the x,y, and z coordinates.

    """
    #extract the parameters
    x_centre, y_centre, z_centre, radius = parameters

    #use numpy's sqrt function here, which works by element on arrays
    distance_from_centre = numpy.sqrt((x_values - x_centre)**2 +
                                      (y_values - y_centre)**2 +
                                      (z_values - z_centre)**2)
    return distance_from_centre - radius
