from setuptools import setup, find_packages

setup(
    name="graph-physics",
    version="0.0.1",
    packages=["graphphysics"],
    entry_points={"console_scripts": ["grph=graphphysics.train:main"]},
)
