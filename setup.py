from setuptools import setup, find_namespace_packages

setup(
    name="graph-physics",
    version="0.0.1",
    # subpackages have no __init__.py, so they must be collected as namespace packages
    packages=find_namespace_packages(include=["graphphysics*"]),
    entry_points={"console_scripts": ["grph=graphphysics.train:main"]},
)
