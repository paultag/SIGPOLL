#!/usr/bin/env python

from sigpoll import __appname__, __version__
from setuptools import setup, find_packages

long_description = ""

setup(
    name=__appname__,
    version=__version__,
    packages=find_packages(),

    author="Paul Tagliamonte",
    author_email="tag@pault.ag",

    long_description=long_description,
    description='such sigpoll',
    license="GPLv3",
    url="https://pault.ag/",

    entry_points={
        'console_scripts': [
            'sigpolld = sigpoll.cli:daemon',
        ]
    },

    platforms=['any']
)
