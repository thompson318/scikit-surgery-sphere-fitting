# coding=utf-8

"""scikit-surgery-sphere-fitting tests"""

import numpy
from sksurgeryvtk.models.vtk_surface_model import VTKSurfaceModel
from sksurgeryspherefitting.algorithms import sphere_fitting
import six

# Pytest style

def test_fit_sphere_least_squares():

    x_centre = 1.74839
    y_centre = 167.0899222
    z_centre = 200.738829

    radius = 7.543589

    #some arrays to fit data to
    xs=numpy.ndarray(shape=(1000,),dtype=float )
    ys=numpy.ndarray(shape=(1000,),dtype=float )
    zs=numpy.ndarray(shape=(1000,),dtype=float )

    #fill the arrays with points uniformly spread on
    #a sphere centred at x,y,z with radius radius
    #first seed the random generator so we get consistent test behaviour
    numpy.random.seed(seed=0)
    for i in range(1000):
        #make a random vector
        x=numpy.random.uniform(-1.0, 1.0)
        y=numpy.random.uniform(-1.0, 1.0)
        z=numpy.random.uniform(-1.0, 1.0)

        #scale it to length radius
        length=numpy.sqrt( (x)**2 + (y)**2 + (z)**2 )
        factor = radius / length

        xs[i] = x*factor + x_centre
        ys[i] = y*factor + y_centre
        zs[i] = z*factor + z_centre

    parameters = [0.0, 0.0, 0.0, 0.0]
    result = sphere_fitting.fit_sphere_least_squares (xs, ys, zs, parameters)
    numpy.testing.assert_approx_equal (result.x[0],  x_centre, significant = 10)
    numpy.testing.assert_approx_equal (result.x[1],  y_centre, significant = 10)
    numpy.testing.assert_approx_equal (result.x[2],  z_centre, significant = 10)
    numpy.testing.assert_approx_equal (result.x[3],  radius, significant = 10)

def test_fit_sphere_to_ct_regression_test1():
    parameters = [0.0, 0.0, 0.0, 0.0]
    parameters = [136.0, 151.0, -91.0, 8.0]
    model = VTKSurfaceModel("data/CT_Level_1.vtp", [1., 0., 0.])
    x_values = model.get_points_as_numpy()[:, 0]
    y_values = model.get_points_as_numpy()[:, 1]
    z_values = model.get_points_as_numpy()[:, 2]
    result = sphere_fitting.fit_sphere_least_squares(x_values,
                                                     y_values,
                                                     z_values,
                                                     parameters)
    numpy.testing.assert_approx_equal (result.x[0],  136.571, significant = 3)
    numpy.testing.assert_approx_equal (result.x[1],  151.973, significant = 3)
    numpy.testing.assert_approx_equal (result.x[2],  -95.518, significant = 3)
    numpy.testing.assert_approx_equal (result.x[3],  8.119, significant = 3)


