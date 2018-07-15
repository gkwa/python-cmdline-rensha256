# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup

import sys
if sys.version_info < (3, 0):
    sys.exit('Sorry, Python < 3.0 is not supported')

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('rensha256/rensha256.py').read(),
    re.M
).group(1)


with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name="cmdline-rensha256",
    python_requires='>3',
    packages=["rensha256"],
    entry_points={
        "console_scripts": ['rensha256 = rensha256.rensha256:main']
    },
    install_requires=[
        "pathlib"
    ],
    version=version,
    description="Python command line application bare bones template.",
    long_description=long_descr,
    url="https://github.com/taylormonacelli/rensha256",
    author="Taylor Monacelli",
    author_email="taylormonacelli@gmail.com"
)
