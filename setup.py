#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Setup script for autoWeCom
"""

from setuptools import setup, find_packages
import os
import sys

# Add the current directory to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import version
from config.settings import APP_VERSION

setup(
    name="autoWeCom",
    version=APP_VERSION,
    description="Automated WeChat Work Interaction Application",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "wxPython>=4.2.0",
    ],
    entry_points={
        "console_scripts": [
            "autowecom=main:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Office/Business",
    ],
) 