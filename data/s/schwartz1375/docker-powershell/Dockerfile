FROM ubuntu  
  
MAINTAINER Matthew Schwartz "@schwartz1375"  
RUN apt-get update && apt-get -y -q install vim wget libunwind8 libicu55  
  
RUN wget
https://github.com/PowerShell/PowerShell/releases/download/v6.0.0-alpha.9/powershell_6.0.0-alpha.9-1ubuntu1.16.04.1_amd64.deb  
  
RUN dpkg -i powershell_6.0.0-alpha.9-1ubuntu1.16.04.1_amd64.deb  
  
CMD ["/bin/bash"]  
  

