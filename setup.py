# coding=utf-8
"""
Setup for scikit-surgery-sphere-fitting
"""

from setuptools import setup, find_packages
import versioneer

# Get the long description
with open('README.rst') as f:
    long_description = f.read()

setup(
    name='scikit-surgery-sphere-fitting',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='scikit-surgery-sphere-fitting implements a least squares sphere fitting algorithm, to read a vtk poly data file, a config file, and outputs the fitted sphere',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/thompson318/scikit-surgery-sphere-fitting',
    author='Stephen Thompson',
    author_email='s.thompson@ucl.ac.uk',
    license='BSD-3 license',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',


        'License :: OSI Approved :: BSD License',


        'Programming Language :: Python',
        'Programming Language :: Python :: 3',

        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
    ],

    keywords='medical imaging',

    packages=find_packages(
        exclude=[
            'doc',
            'tests',
            'data'
        ]
    ),

    install_requires=[
        'numpy>=1.11',
        'scipy',
        'vtk<9.0',
        'scikit-surgeryvtk'
    ],

    entry_points={
        'console_scripts': [
            'sksurgeryspherefitting=sksurgeryspherefitting.__main__:main',
        ],
    },
)
