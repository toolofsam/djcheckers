from setuptools import setup, find_packages
from setuptools.command.install import install


setup(
    name='gameboard',
    version='0.1',
    description="Checkers game board and logic",
    keywords='',
    author='',
    author_email='',
    url='',
    package_dir={'gameboard': 'gameboard'},
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
)
