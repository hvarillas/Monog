from setuptools import setup, find_packages
# import codecs
# import os

VERSION = '0.0.1'
DESCRIPTION = 'Logger and monitoring'
LONG_DESCRIPTION = 'Logger and monitoring'

# Setting up
setup(
    name='monog',
    version=VERSION,
    author='Hernán Varillas',
    author_email='hernan.varillas93@gmail.com',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=['testing']),
    install_requires=[],
    keywords=['python', 'log', 'monitoring'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"
    ]
)