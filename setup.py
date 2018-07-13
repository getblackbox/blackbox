from setuptools import setup, find_packages
import blackbox
import os

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='blackbox',
    version='0.0.1',
    description='An implementation of machine learning potentials for MD simulations',
    long_description=readme(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords=['machine learnig', 'blackbox', 'molecular dynamics'],
    url='https://getblackbox.org/',
    license='GNU',
    packages=find_packages(),
    install_requires=[
        'numpy',
    ],
)