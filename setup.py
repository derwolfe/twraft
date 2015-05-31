"""
Setup file for twraft 
"""

from setuptools import setup, find_packages

setup(
    name='twraft',
    version='0.1.0',
    description="""
    An implementation of the Raft consensus algorithm using Twisted
    """,
    packages=find_packages(exclude=[]),
    package_dir={'twraft': 'twraft'},
    install_requires=[
    ],
    include_package_data=True,
    license="MIT"
)
