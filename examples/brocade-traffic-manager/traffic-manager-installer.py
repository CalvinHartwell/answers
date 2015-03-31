#==============================================================================
# Answers Python Library - Brocade Traffic Manager Installer Example (Riverbed)
# Copyright Calvin Hartwell 2015. 
# Distributed under the MIT License.
# (See accompanying file LICENSE or copy at http://opensource.org/licenses/MIT)
#==============================================================================

from answers import *

# Riverbed Traffic Manager Automatic Installer - Version 9.9

# Download Traffic Manager Repo from archive using wget (Riverbed/Brocade url is tgz archive for traffic manager 9.9)
TrafficManagerRepo = Answers('wget http://support.riverbed.com/bin/support/download?sid=89ckt05tr2m4htokv1sphofgt3 -O ZeusTM_latest.tgz')
TrafficManagerRepo.debugMode = True
TrafficManagerRepo.timeoutInSeconds = 25
TrafficManagerRepo.Execute()

# Extract file (may vary on os)
ExtractTrafficManager = Answers('tar -zxvf ZeusTM_latest.tgz --directory /usr/tmp/')
ExtractTrafficManager.debugMode = True
ExtractTrafficManager.Execute()

# Create user group lbalancer
CreateGroup = Answers('groupadd lbalancer')
CreateGroup.debugMode = True
CreateGroup.timeoutInSeconds = 5
CreateGroup.Execute()

# Create user lbalancer
CreateUser = Answers('useradd -g lbalancer -s /sbin/nologin lbalancer')
CreateUser.debugMode = True
CreateUser.timeoutInSeconds = 5
CreateUser.Execute()

# Install and configure traffic manager
TrafficManagerInstall = Answers('/usr/tmp/ZeusTM_99_Linux-x86_64/zinstall', 'traffic-manager-answers.json')
TrafficManagerInstall.debugMode = True
TrafficManagerInstall.defaultAnswerMode = False
TrafficManagerInstall.logMode = True
TrafficManagerInstall.timeoutInSeconds = 10
TrafficManagerInstall.Execute()

# Traffic Manager GUI should now be running on http://fqdn:9090
