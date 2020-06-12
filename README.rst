scikit-surgery-sphere-fitting
=============================

.. image:: https://github.com/thompson318/scikit-surgery-sphere-fitting/raw/master/project-icon.png
   :height: 128px
   :width: 128px
   :target: https://github.com/thompson318/scikit-surgery-sphere-fitting
   :alt: Logo

.. image:: https://github.com/thompson318/scikit-surgery-sphere-fitting/workflows/.github/workflows/ci.yml/badge.svg
   :target: https://github.com/thompson318/scikit-surgery-sphere-fitting/actions
   :alt: GitHub Actions CI status

.. image:: https://coveralls.io/repos/github/thompson318/scikit-surgery-sphere-fitting/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/thompson318/scikit-surgery-sphere-fitting?branch=master
    :alt: Test coverage

.. image:: https://readthedocs.org/projects/scikit-surgery-sphere-fitting/badge/?version=latest
    :target: http://scikit-surgery-sphere-fitting.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://zenodo.org/badge/259240969.svg
   :target: https://zenodo.org/badge/latestdoi/259240969
   :alt: DOI - zenodo

Author: Stephen Thompson

scikit-surgery-sphere-fitting is part of the `SciKit-Surgery`_ software project, developed at the `Wellcome EPSRC Centre for Interventional and Surgical Sciences`_, part of `University College London (UCL)`_.

scikit-surgery-sphere-fitting supports Python 3.6.

scikit-surgery-sphere-fitting fits a sphere to a set of 3D points. It includes a user interface that
will read data from a vtk polydata file create an output polydata file showing the fitted sphere.
Example usage:

::

    python sksurgeryspherefitting.py polydata_in.vtp --output polydatata_out.vtp --config conf.json

It was created in part to provide a simple demonstration of algorithm development as part of a
program of SNAPPY Tutorials, but also provides a useful service should you want to fit a sphere
to some data.

Citing
------
If you use SciKit-Surgery-Sphere-Fitting in your research or teaching please cite it. Individual releases can be cited via the Zenodo tag above. SciKit-Surgery should be cited as:

Thompson S, Dowrick T, Ahmad M, et al. "SciKit-Surgery: compact libraries for surgical navigation." International Journal of Computer Assisted Radiology and Surgery. 2020 May. DOI: `10.1007/s11548-020-02180-5`_.


Developing
----------

Cloning
^^^^^^^

You can clone the repository using the following command:

::

    git clone https://github.com/thompson318/scikit-surgery-sphere-fitting


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

    pip install git+https://github.com/thompson318/scikit-surgery-sphere-fitting

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
.. _`source code repository`: https://github.com/thompson318/scikit-surgery-sphere-fitting
.. _`Documentation`: https://scikit-surgery-sphere-fitting.readthedocs.io
.. _`SciKit-Surgery`: https://github.com/UCL/scikit-surgery/wiki
.. _`University College London (UCL)`: http://www.ucl.ac.uk/
.. _`Wellcome`: https://wellcome.ac.uk/
.. _`EPSRC`: https://www.epsrc.ac.uk/
.. _`contributing guidelines`: https://github.com/thompson318/scikit-surgery-sphere-fitting/blob/master/CONTRIBUTING.rst
.. _`license file`: https://github.com/thompson318/scikit-surgery-sphere-fitting/blob/master/LICENSE
.. _`10.1007/s11548-020-02180-5`: https://doi.org/10.1007/s11548-020-02180-5
