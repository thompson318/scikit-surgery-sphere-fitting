# coding=utf-8

"""Command line processing"""


import argparse
from sksurgeryspherefitting import __version__
from sksurgeryspherefitting.ui.sksurgeryspherefitting_demo import run_demo


def main(args=None):
    """Entry point for scikit-surgery-sphere-fitting application"""

    parser = argparse.ArgumentParser(
        description='scikit-surgery-sphere-fitting')

    ## ADD POSITIONAL ARGUMENTS
    parser.add_argument("model",
                        type=str,
                        help="Filename for vtk surface model")

    # ADD OPTINAL ARGUMENTS
    parser.add_argument("-o", "--output",
                        required=False,
                        type=str,
                        default="",
                        help="Write the fitted sphere to file"
                        )

    version_string = __version__
    friendly_version_string = version_string if version_string else 'unknown'
    parser.add_argument(
        "--version",
        action='version',
        version='scikit-surgery-sphere-fitting version '
        + friendly_version_string
        )

    args = parser.parse_args(args)

    run_demo(args.model, args.output)
