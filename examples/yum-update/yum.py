#=======================================================================
# Answers Python Library. 
# Copyright Calvin Hartwell 2015. 
# Distributed under the MIT License.
# (See accompanying file LICENSE or copy at http://opensource.org/licenses/MIT)
#=======================================================================

from answers import *
						# Automatically answer yes to install any packages, the same as sudo yum -y update
ShellCommand = Answers("sudo yum update", '{"answers": [ {"question":"Is this ok [y/d/N]", "answer":"y"}] }')
ShellCommand.debugMode = True
ShellCommand.logMode = True
ShellCommand.timeoutInSeconds = 1
ShellCommand.Execute()
