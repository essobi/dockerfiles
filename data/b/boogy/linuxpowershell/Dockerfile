FROM ubuntu:latest  
MAINTAINER boogy theboogymaster@gmail.com  
  
LABEL Name="ubuntu/LinuxPowerShell"  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt update \  
&& apt -yq upgrade \  
&& apt -yq install \  
git wget libunwind8 libicu55 libcurl3  
  
RUN useradd --create-home --shell /bin/bash poweruser  
RUN wget -q
https://github.com/PowerShell/PowerShell/releases/download/v6.0.0-beta.4/powershell_6.0.0-beta.4-1ubuntu1.16.04.1_amd64.deb
-O powershell.deb \  
&& dpkg -i powershell.deb \  
&& apt-get install -f \  
&& rm -f $_  
  
USER poweruser  
  
RUN mkdir -p /home/poweruser/.local/share/powershell/Modules/ \  
&& git clone https://github.com/PowerShellMafia/PowerSploit.git
/home/poweruser/.local/share/powershell/Modules/PowerSploit  
  
WORKDIR /home/poweruser  
  
CMD [ "/usr/bin/powershell" ]  

