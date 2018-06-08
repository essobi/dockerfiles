FROM centos:latest  
LABEL MAINTAINER="Frederic Jacquet <fred@ljf.ch>"  
# Register the Microsoft RedHat repository  
RUN cd /etc/yum.repos.d/ && curl -L -O
https://packages.microsoft.com/config/rhel/7/prod.repo  
RUN yum install -y --setopt=tsflags=nodocs deltarpm powershell unzip && yum -y
--setopt=tsflags=nodocs update && yum clean all  
RUN curl
https://communities.cisco.com/servlet/JiveServlet/download/74217-3-149644/ucspowertoolcore.zip
-o /tmp/ucspowertoolcore.zip  
RUN mkdir -p /root/.local/share/powershell/Modules && unzip
/tmp/ucspowertoolcore.zip -d /root/.local/share/powershell/Modules && rm -rf
/tmp/ucspowertoolcore.zip  
RUN pwsh -ex unrestricted -noni -Command Set-PSRepository -Name PSGallery
-InstallationPolicy Trusted  
RUN pwsh -ex unrestricted -noni -Command Install-Module -name PSExcel  
RUN pwsh -ex unrestricted -noni -Command Install-Module -name VMware.PowerCLI  
RUN pwsh -ex unrestricted -noni -Command Install-Module -Name PowerNSX  
RUN pwsh -ex unrestricted -noni -Command Install-Module -Name VPLEX-Powershell  
RUN pwsh -ex unrestricted -noni -Command Install-Module -Name Unity-Powershell  
RUN pwsh -ex unrestricted -noni -Command Install-Module -Name IsilonPlatform  
# Start PowerShell  
ENTRYPOINT [ "pwsh" ]  
#CMD [ "/bin/bash" ]

