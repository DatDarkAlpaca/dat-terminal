from setuptools import find_packages, setup

setup(
    name='dat-terminal',
    author='DatDarkAlpaca',
    description='An interactive terminal for applications that needs custom commands.',
    license='MIT',
    url='https://github.com/DatDarkAlpaca/dat-terminal',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'PyYAML',
        'colorama',
        'termcolor'
    ],
    python_requires='>=3.8.0',
)
