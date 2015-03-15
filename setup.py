from setuptools import setup, find_packages # prefer setuptools over distutils
from codecs import open 					# to use a consistent encoding
from os import path 						

# path to current workign direcy
currentDirectory = path.abspath(path.dirname(__file__))

# load long description file 
with open(path.join(currentDirectory, 'DESCRIPTION.rst'), encoding='utf-8') as fileInCWD:
	long_description = fileInCWD.read()

setup (
	name='answers', 
	packages=['answers'],
	version='0.0.3.a1',

	description='Library for automating command line processes and installers',
	long_description = long_description, 

	author='Calvin Hartwell',
	author_email='mail@calvinhartwell.com',
	url='https://github.com/calvinhartwell/answers',

	license='MIT', # Please do whatever you want with this library

	classifiers=['Development Status :: 3 - Alpha',
				'Intended Audience :: Developers', 
				'Topic :: System :: Installation/Setup',
				'License :: OSI Approved :: MIT License', 
				'Programming Language :: Python :: 2',
				'Programming Language :: Python :: 2.6',
				'Programming Language :: Python :: 2.7',
				'Programming Language :: Python :: 3',
				'Programming Language :: Python :: 3.2',
				'Programming Language :: Python :: 3.3',
				'Programming Language :: Python :: 3.4'],

	keywords='automate installer command line shell automation automatic',

	entry_points={
		'console_scripts': ['answers=answers:main'],
	},
)