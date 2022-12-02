from setuptools import find_packages, setup

DESCRIPTION = 'An interactive terminal for applications that needs custom commands.'
VERSION = '0.0.1'


setup(
    name='dat-terminal',
    author='DatAlpaca',
    description=DESCRIPTION,
    license='MIT',
    url='https://github.com/DatDarkAlpaca/dat-terminal',
    version=VERSION,
    packages=find_packages(),
    install_requires=[
        'PyYAML',
        'colorama',
        'termcolor'
    ],
    python_requires='>=3.8.0',
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Typing :: Typed',
      ]
)
