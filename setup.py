#!/usr/bin/env python

#from distutils.core import setup
from setuptools import find_packages, setup
import Image2Anime

install_requires = [
    'requests',
    'urllib3',
]

packages = [
    'Image2Anime'
]

setup(
    name="Image2Anime",
    version=Image2Anime.__version__,
    description="Search your anime scene by just " \
                "an image! :D",
    author="Anysz, Soruly",
    author_email="anyoneelsegg@gmail.com",
    url="https://trace.moe",
    packages=packages,
    license="MIT License",
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.0",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Topic :: Internet",
        "Topic :: Multimedia :: Video"
    ],
)
