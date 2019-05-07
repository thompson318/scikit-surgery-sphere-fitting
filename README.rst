scikit-surgery-sphere-fitting
===============================

.. image:: https://weisslab.cs.ucl.ac.uk/StephenThompson/scikit-surgery-sphere-fitting/raw/master/project-icon.png
   :height: 128px
   :width: 128px
   :target: https://weisslab.cs.ucl.ac.uk/StephenThompson/scikit-surgery-sphere-fitting
   :alt: Logo

.. image:: https://weisslab.cs.ucl.ac.uk/StephenThompson/scikit-surgery-sphere-fitting/badges/master/build.svg
   :target: https://weisslab.cs.ucl.ac.uk/StephenThompson/scikit-surgery-sphere-fitting/pipelines
   :alt: GitLab-CI test status

.. image:: https://weisslab.cs.ucl.ac.uk/StephenThompson/scikit-surgery-sphere-fitting/badges/master/coverage.svg
    :target: https://weisslab.cs.ucl.ac.uk/StephenThompson/scikit-surgery-sphere-fitting/commits/master
    :alt: Test coverage

.. image:: https://readthedocs.org/projects/scikit-surgery-sphere-fitting/badge/?version=latest
    :target: http://scikit-surgery-sphere-fitting.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status



Author: Stephen Thompson

scikit-surgery-sphere-fitting is part of the `SNAPPY`_ software project, developed at the `Wellcome EPSRC Centre for Interventional and Surgical Sciences`_, part of `University College London (UCL)`_.

scikit-surgery-sphere-fitting supports Python 3.6.

scikit-surgery-sphere-fitting fits a sphere to a set of 3D points. It includes a user interface that
will read data from a vtk polydata file create an output polydata file showing the fitted sphere.
Example usage:

::

    python sksurgeryspherefitting.py polydata_in.vtp --output polydatata_in.vtp

It was created in part to provide a simple demonstration of algorithm development as part of a
program of SNAPPY Tutorials, but also provides a useful service should you want to fit a sphere
to some data.

Developing
----------

Cloning
^^^^^^^

You can clone the repository using the following command:

::

    git clone https://weisslab.cs.ucl.ac.uk/StephenThompson/scikit-surgery-sphere-fitting


Running tests
^^^^^^^^^^^^^
Pytest is used for running unit tests:
::

    pip install pytest
    python -m pytest


Linting
^^^^^^^

This code conforms to the PEP8 standard. Pylint can be used to analyse the code:

::

    pip install pylint
    pylint --rcfile=tests/pylintrc sksurgeryspherefitting


Installing
----------

You can pip install directly from the repository as follows:

::

    pip install git+https://weisslab.cs.ucl.ac.uk/StephenThompson/scikit-surgery-sphere-fitting

or directly from pypi

::
   
   pip install scikit-surgery-sphere-fitting


Contributing
^^^^^^^^^^^^

Please see the `contributing guidelines`_.


Useful links
^^^^^^^^^^^^

* `Source code repository`_
* `Documentation`_


Licensing and copyright
-----------------------

Copyright 2019 University College London.
scikit-surgery-sphere-fitting is released under the BSD-3 license. Please see the `license file`_ for details.


Acknowledgements
----------------

Supported by `Wellcome`_ and `EPSRC`_.


.. _`Wellcome EPSRC Centre for Interventional and Surgical Sciences`: http://www.ucl.ac.uk/weiss
.. _`source code repository`: https://weisslab.cs.ucl.ac.uk/StephenThompson/scikit-surgery-sphere-fitting
.. _`Documentation`: https://scikit-surgery-sphere-fitting.readthedocs.io
.. _`SNAPPY`: https://weisslab.cs.ucl.ac.uk/WEISS/PlatformManagement/SNAPPY/wikis/home
.. _`University College London (UCL)`: http://www.ucl.ac.uk/
.. _`Wellcome`: https://wellcome.ac.uk/
.. _`EPSRC`: https://www.epsrc.ac.uk/
.. _`contributing guidelines`: https://weisslab.cs.ucl.ac.uk/StephenThompson/scikit-surgery-sphere-fitting/blob/master/CONTRIBUTING.rst
.. _`license file`: https://weisslab.cs.ucl.ac.uk/StephenThompson/scikit-surgery-sphere-fitting/blob/master/LICENSE

