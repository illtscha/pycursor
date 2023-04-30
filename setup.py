from setuptools import setup, find_packages

setup(
    name='pycursor',
    version='0.2',
    packages=find_packages(),
    entry_points={
            'console_scripts': [
                'pycursor=pycursor:main'
            ]
        }
)