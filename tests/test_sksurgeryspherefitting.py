# coding=utf-8

"""scikit-surgery-sphere-fitting tests"""

import numpy
from sksurgeryvtk.models.vtk_surface_model import VTKSurfaceModel
from sksurgeryspherefitting.algorithms import sphere_fitting

# Pytest style

def test_fit_sphere_least_squares():
    """Test that it fits a sphere with some gaussian noise"""
    x_centre = 1.74839
    y_centre = 167.0899222
    z_centre = 200.738829

    radius = 7.543589

    #some arrays to fit data to
    x_values = numpy.ndarray(shape=(1000,), dtype=float)
    y_values = numpy.ndarray(shape=(1000,), dtype=float)
    z_values = numpy.ndarray(shape=(1000,), dtype=float)

    #fill the arrays with points uniformly spread on
    #a sphere centred at x,y,z with radius radius
    #first seed the random generator so we get consistent test behaviour
    numpy.random.seed(seed=0)
    for i in range(1000):
        #make a random vector
        x_vector = numpy.random.uniform(-1.0, 1.0)
        y_vector = numpy.random.uniform(-1.0, 1.0)
        z_vector = numpy.random.uniform(-1.0, 1.0)

        #scale it to length radius
        length = numpy.sqrt((x_vector)**2 + (y_vector)**2 + (z_vector)**2)
        factor = radius / length

        x_values[i] = x_vector*factor + x_centre
        y_values[i] = y_vector*factor + y_centre
        z_values[i] = z_vector*factor + z_centre

    parameters = [0.0, 0.0, 0.0, 0.0]
    result = sphere_fitting.fit_sphere_least_squares(x_values, y_values,
                                                     z_values, parameters)
    numpy.testing.assert_approx_equal(result.x[0], x_centre, significant=10)
    numpy.testing.assert_approx_equal(result.x[1], y_centre, significant=10)
    numpy.testing.assert_approx_equal(result.x[2], z_centre, significant=10)
    numpy.testing.assert_approx_equal(result.x[3], radius, significant=10)

def test_regression_test1():
    """A regression test with manually init"""
    parameters = [136.0, 151.0, -91.0, 8.0]
    model = VTKSurfaceModel("data/CT_Level_1.vtp", [1., 0., 0.])
    x_values = model.get_points_as_numpy()[:, 0]
    y_values = model.get_points_as_numpy()[:, 1]
    z_values = model.get_points_as_numpy()[:, 2]
    result = sphere_fitting.fit_sphere_least_squares(x_values,
                                                     y_values,
                                                     z_values,
                                                     parameters)
    numpy.testing.assert_approx_equal(result.x[0], 136.571, significant=3)
    numpy.testing.assert_approx_equal(result.x[1], 151.973, significant=3)
    numpy.testing.assert_approx_equal(result.x[2], -95.518, significant=3)
    numpy.testing.assert_approx_equal(result.x[3], 8.119, significant=3)

def test_regression_test2():
    """A regression test with fixed radius"""
    model = VTKSurfaceModel("data/US_Sphere_2.vtp", [1., 0., 0.])
    x_values = model.get_points_as_numpy()[:, 0]
    y_values = model.get_points_as_numpy()[:, 1]
    z_values = model.get_points_as_numpy()[:, 2]
    parameters = [numpy.mean(x_values), numpy.mean(y_values),
                  numpy.mean(z_values), 4.5]
    radius = 4.5
    epsilon = 1e-6
    bounds = ((-numpy.inf, -numpy.inf, -numpy.inf, radius-epsilon),
              (numpy.inf, numpy.inf, numpy.inf, radius+epsilon))
    result = sphere_fitting.fit_sphere_least_squares(x_values,
                                                     y_values,
                                                     z_values,
                                                     parameters,
                                                     bounds=bounds)
    numpy.testing.assert_approx_equal(result.x[0], 86.474, significant=3)
    numpy.testing.assert_approx_equal(result.x[1], -97.243, significant=3)
    numpy.testing.assert_approx_equal(result.x[2], -208.528, significant=3)
    numpy.testing.assert_approx_equal(result.x[3], 4.500, significant=3)
