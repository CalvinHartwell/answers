#=======================================================================
# Answers Python Library. 
# Copyright Calvin Hartwell 2015. 
# Distributed under the MIT License.
# (See accompanying file LICENSE or copy at http://opensource.org/licenses/MIT)
#=======================================================================

from answers import *

ShellCommand = Answers("uname -a")
ShellCommand.debugMode = True
ShellCommand.logMode = True
ShellCommand.timeoutInSeconds = 1
ShellCommand.Execute()
