FROM ubuntu:latest  
LABEL MAINTAINER="Alan Scott"  
RUN apt-get update && apt-get -y install libunwind8 libicu55 wget libcurl3
liblttng-ust0  
RUN wget -q
https://github.com/PowerShell/PowerShell/releases/download/v6.0.0-rc/powershell_6.0.0-rc-1.ubuntu.16.04_amd64.deb  
RUN dpkg -i powershell_6.0.0-rc-1.ubuntu.16.04_amd64.deb && rm
powershell_6.0.0-rc-1.ubuntu.16.04_amd64.deb  
RUN echo "New-PSDrive -Name C -PSProvider FileSystem -Root /" >
/opt/microsoft/powershell/6.0.0-rc/profile.ps1  
CMD pwsh

