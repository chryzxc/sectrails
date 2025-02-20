# filepath: setup.py
from setuptools import setup, find_packages

setup(
    name="sectrails",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
        "tabulate"
    ],
    entry_points={
        "console_scripts": [
            "sectrails=sectrails.main:main",
        ],
    },
    author="Christian Villablanca",
    author_email="chriztiann.villablanca@gmail.com",
    description="A tool to fetch DNS history from SecurityTrails using cli",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/chryzxc/sectrails",
)