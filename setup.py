#! /usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="diskprojection",
    version="0.4",
    author="Richard Teague",
    author_email="richard.d.teague@cfa.harvard.edu",
    description=("Infer and reproject a disk's 3D structure."),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/richteague/diskprojection",
    packages=["diskprojection"],
    license="MIT",
    install_requires=[
        "scipy",
        "numpy",
        "matplotlib",
        "gofish",
        "astropy",
        "emcee",
        ],
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
