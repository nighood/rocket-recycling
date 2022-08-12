import os
import re
from codecs import open
from distutils.core import setup

from setuptools import find_packages

def _load_req(file: str):
    with open(file, 'r', 'utf-8') as f:
        return [line.strip() for line in f.readlines() if line.strip()]

requirements = _load_req('Requirements.txt')

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    # information
    name="rocket_recycling",
    version="0.1",
    packages=find_packages(),   # or ['rocket_recycling']
    package_data={
        package_name: ['*.jpg']
        for package_name in find_packages(include=('*'))
    },
    description="A simple rocket env for RL.",
    long_description=readme,
    long_description_content_type='text/markdown',
    author='DI-Engine',
    author_email='opendilab.contact@gmail.com',
    license='Apache License, Version 2.0',
    keywords='A simple rocket env for RL.',
    url='https://github.com/nighood/rocket-recycling',

    # environment
    python_requires=">=3.7",
    install_requires=requirements,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)