Answers - Python Pip Library
===============================

This is a Python Pip (Pypi) library used to automate shell commands and other unix processes.

When combined with a configuration management tool, such as Puppet or Chef, this library should be very powerful. 

Installation with Pip (Pypi):
===============================

The library can either be installed from source or through Python Pip. First ensure that Pip is installed, running either of the commands as root (or using sudo): 

	CentOS/Redhat Linux/Oracle Enterprise Linux/Fedora: 
			yum install python-pip 
			
	Ubuntu/Debian: 
			apt-get install python-pip


After you've installed Pip, the next step is to install the answers library:

	pip install answers

To install the current development version of the library, use the following command: 

	pip install answers --pre
	
You can also install the library using Pip with a local copy of the library, to do that, CD into the directory and then run:

	pip install .
	
This will install the version of the library in the directory. If the same version or another version is already installed, run this command to upgrade it:

	pip install . --upgrade
	
Manual installation without Pip (Pypi):
=========================================

To install the library without Pip, download the library (from Pypi or Github) and then CD into the folder. 

Run the following command: 

	python setup.py install
	
The library should now be installed. 
	
Using the library:
===============================

The library includes various code examples which demonstrate how the library is used. The example scripts can be found within the examples directory. 

Here is the most basic example of utilising the script to execute the uname shell command: 

	from answers import *

	ShellCommand = Answers("uname -a")
	ShellCommand.Execute()

The library can also be used to execute a process which requires user input, by answering any questions presented to the user automatically. 

Answers file JSON format: 
===============================

The answers for the particular installer/process should be in the following format within a json file or string: 

	{ "answers": 
		[
			{ 
				"question": "Do you wish to continue:", 
				"answer": "y"
			},
		]
	}

The questions should be within the answers array, and each question should have a default answer, even if it is blank. 

To execute a process with the answers file loaded, use the following: 

	AutomatedInstaller = Answers('/path/to/executable', '/path/to/answers.json')
	AutomatedInstaller.Execute()

For a worked example of this, see the Brocade Traffic Manager installer script within the examples folder. 
 
