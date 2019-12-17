# coding=utf-8

"""Uses sphere fitting to fit to vtk model"""
import vtk
from numpy import inf, mean, std
from sksurgeryvtk.models.vtk_surface_model import VTKSurfaceModel
from sksurgerycore.configuration.configuration_manager import (
        ConfigurationManager
        )
from sksurgeryspherefitting.algorithms import sphere_fitting

def run_demo(model_file_name, output="", configfile=False):
    """ Run the application """
    model = VTKSurfaceModel(model_file_name, [1., 0., 0.])
    x_values = model.get_points_as_numpy()[:, 0]
    y_values = model.get_points_as_numpy()[:, 1]
    z_values = model.get_points_as_numpy()[:, 2]

    initial_parameters = [mean(x_values), mean(y_values), mean(z_values),
                          std(x_values)]
    bounds = ((-inf, -inf, -inf, -inf),
              (inf, inf, inf, inf))

    if configfile:
        configurer = ConfigurationManager(configfile)
        configuration = configurer.get_copy()
        if "initial values" in configuration:
            initial_parameters = configuration.get("initial values")
        if "bounds" in configuration:
            bounds = configuration.get("bounds")
        if "fixed radius" in configuration:
            radius = configuration.get("fixed radius")
            bounds = ((-inf, -inf, -inf, radius - 1e-6),
                      (inf, inf, inf, radius + 1e-6))

    result = sphere_fitting.fit_sphere_least_squares(x_values,
                                                     y_values,
                                                     z_values,
                                                     initial_parameters,
                                                     bounds=bounds)

    print("Result is {}".format(result))

    if output != "":

        sphere = vtk.vtkSphereSource()
        sphere.SetCenter(result.x[0], result.x[1], result.x[2])
        sphere.SetRadius(result.x[3])
        sphere.SetThetaResolution(60)
        sphere.SetPhiResolution(60)

        writer = vtk.vtkXMLPolyDataWriter()
        writer.SetFileName(output)
        writer.SetInputData(sphere.GetOutput())
        sphere.Update()
        writer.Write()
