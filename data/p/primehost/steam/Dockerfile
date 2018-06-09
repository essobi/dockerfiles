FROM primehost/ubuntu-core  
MAINTAINER Prime-Host <info@nordloh-webdesign.de>  
  
# update before install  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# Install dependencies  
RUN apt-get install -y lib32gcc1 lsof  
  
# Run commands as the steam user  
RUN adduser \  
\--disabled-login \  
\--shell /bin/bash \  
\--gecos "" \  
steam  
  
# Add to sudo group  
RUN usermod -a -G sudo steam  
  
# download steamcmd  
RUN mkdir /home/steam/steamcmd &&\  
cd /home/steam/steamcmd &&\  
curl http://media.steampowered.com/installer/steamcmd_linux.tar.gz | tar -vxz  
  
# clean up unneeded packages  
RUN apt-get --purge autoremove -y  

