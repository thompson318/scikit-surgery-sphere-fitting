# coding=utf-8

"""Uses sphere fitting to fit to vtk model"""
import vtk
from sksurgeryvtk.models.vtk_surface_model import VTKSurfaceModel
from sksurgeryspherefitting.algorithms import sphere_fitting

def run_demo(model_file_name, output=""):
    """ Run the application """
    model = VTKSurfaceModel(model_file_name, [1., 0., 0.])
    x_values = model.get_points_as_numpy()[:, 0]
    y_values = model.get_points_as_numpy()[:, 1]
    z_values = model.get_points_as_numpy()[:, 2]

    initial_parameters = [0.0, 0.0, 0.0, 0.0]
    result = sphere_fitting.fit_sphere_least_squares(x_values,
                                                     y_values,
                                                     z_values,
                                                     initial_parameters)

    print("Result is {}".format(result))

    if output != "":

        sphere = vtk.vtkSphereSource()
        sphere.SetCenter(result[0][0], result[0][1], result[0][2])
        sphere.SetRadius(result[0][3])
        sphere.SetThetaResolution(60)
        sphere.SetPhiResolution(60)

        writer = vtk.vtkXMLPolyDataWriter()
        writer.SetFileName(output)
        writer.SetInputData(sphere.GetOutput())
        sphere.Update()
        writer.Write()
