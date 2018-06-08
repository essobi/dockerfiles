# jenkins:lts is based on Debian 9 (Stretch)  
# For information about how to install PowerShell in Debian 9, see the
following link:  
#
https://github.com/PowerShell/PowerShell/blob/master/docs/installation/linux.md#debian-9  
ARG jenkins_tag=lts  
FROM jenkins/jenkins:${jenkins_tag}  
  
# To run apt  
USER root  
  
# Install required packages  
RUN apt-get update && apt-get install -y apt-transport-https && rm -rf
/var/lib/apt/lists/*  
  
# Install PowerShell from Microsoft’s repository  
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -  
RUN sh -c 'echo "deb [arch=amd64]
https://packages.microsoft.com/repos/microsoft-debian-stretch-prod stretch
main" > /etc/apt/sources.list.d/microsoft.list'  
RUN apt-get update && apt-get install -y powershell && rm -rf
/var/lib/apt/lists/*  
  
# Drop back to the jenkins user  
USER jenkins  

