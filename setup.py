#!/usr/bin/env python

from setuptools import find_packages, setup


setup(
    name="boundary_iou",
    packages=find_packages(),
    version="0.1",
    author="bowencheng",
    python_requires=">=3.6",
    install_requires=[
        "setuptools",
        "cython",
        "numpy",
        "tabulate",
        "fvcore>=0.1.1",
        "pycocotools>=2.0.1",
        "cityscapesscripts>=1.5.0",
        "panopticapi @ https://github.com/cocodataset/panopticapi/archive/master.zip"
    ],
)
