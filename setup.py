from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

setup(
    name='adress_book_test',
    version='0.0.1',
    description='Simple Python package test for Ginger Payments',
    long_description=readme,
    author='Benjamin Rood',
    author_email='benisrood@gmail.com',
    license=None,
    packages=find_packages(exclude='tests'),
    install_requires=['pytest>=3.0.2']
)
