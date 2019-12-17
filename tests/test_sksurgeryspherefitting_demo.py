# coding=utf-8

"""scikit-surgery-sphere-fitting tests"""

from sksurgeryspherefitting.ui.sksurgeryspherefitting_demo import run_demo

def test_fit_sphere_least_sqs_demo():
    """ test the run demo entry point """

    model_name = 'data/CT_Level_1.vtp'
    output_name = 'out_temp.vtp'

    run_demo(model_name, output_name)


def test_fit_sphere_config_demo():
    """ test the run demo entry point """

    model_name = 'data/US_Sphere_2.vtp'
    config_name = 'data/config_init_with_bounds.json'

    run_demo(model_name, configfile=config_name)


def test_fit_sphere_config_rad_demo():
    """ test the run demo entry point """

    model_name = 'data/US_Sphere_2.vtp'
    config_name = 'data/config_fixed_radius.json'

    run_demo(model_name, configfile=config_name)
