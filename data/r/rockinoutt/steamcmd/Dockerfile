FROM centos:7  
# inspired by kmallea/steamcmd  
MAINTAINER Bryan Monsalvatge <dreadnought93@gmail.com>  
  
# Install dependencies  
RUN yum -y install glibc.i686 libgcc_s.so.1 curl wget  
  
# Download and extract SteamCMD  
RUN mkdir -p /home/steam/steamcmd &&\  
cd /home/steam/steamcmd &&\  
curl -s http://media.steampowered.com/installer/steamcmd_linux.tar.gz | tar
-vxz  
  
WORKDIR /home/steam/steamcmd  
  
# This container will be executable  
ENTRYPOINT ["./steamcmd.sh"]  

