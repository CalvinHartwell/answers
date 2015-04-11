#=======================================================================
# Answers Python Library. 
# Copyright Calvin Hartwell 2015. 
# Distributed under the MIT License.
# (See accompanying file LICENSE or copy at http://opensource.org/licenses/MIT)
#=======================================================================

# Will automatically update packages, setup RPMFusion and then install the Steam client to play games.
# Tested on Fedora 21, fresh build with no RPM Fusion setup.  
from answers import *
									
# Automatically answer yes to install any packages, the same as sudo yum -y update (assume executing account on sudo file)
UpdateExistingPackages = Answers("sudo yum update", '{"answers": [ {"question":"Is this ok [y/N]", "answer":"y"},{"question":"Is this ok [y/d/N]", "answer":"y"} ]}')
UpdateExistingPackages.debugMode = True
UpdateExistingPackages.logMode = True
UpdateExistingPackages.timeoutInSeconds = 1
UpdateExistingPackages.Execute()

# Automatically setup the RPM fusion packages for Fedora (tested on Fedora 21 - assume executing account on sudo file)
SetupRPMFusion = Answers("sudo yum localinstall --nogpgcheck http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm", 
						 '{"answers": [ {"question":"Is this ok [y/N]", "answer":"y"},{"question":"Is this ok [y/d/N]", "answer":"y"} ]}')
SetupRPMFusion.debugMode = True
SetupRPMFusion.logMode = True
SetupRPMFusion.timeoutInSeconds = 1
SetupRPMFusion.Execute()

# Automatically install steam (assume executing account on sudo file)
InstallSteam = Answers("sudo yum install steam", '{"answers": [ {"question":"Is this ok [y/N]", "answer":"y"},{"question":"Is this ok [y/d/N]", "answer":"y"} ]}')
InstallSteam.debugMode = True
InstallSteam.logMode = True
InstallSteam.timeoutInSeconds = 1
InstallSteam.Execute()
