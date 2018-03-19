
from setuptools import setup, find_packages
setup(
    name='pyfilemods',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'docutils',
        'path.py',
    ],
    author='@westurner',
    description=(
        'Identify and compare Python file functions/methods and attributes '
        'from os, os.path, shutil, pathlib, and path.py'),
    license='PSF, MIT',
    url='https://github.com/westurner/pyfilemods',
    project_urls={
        'Source': 'https://github.com/westurner/pyfilemods',
        'Documentation': 'https://westurner.github.io/pyfilemods/',
    }
)
