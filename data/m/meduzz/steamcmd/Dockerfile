FROM ubuntu:14.04  
MAINTAINER [Bot] Meduzz <drgevalia@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y curl lib32gcc1 mysql-client-5.6  
  
RUN mkdir -p /opt/steamcmd && \  
curl -s http://media.steampowered.com/installer/steamcmd_linux.tar.gz | tar
-vxz -C /opt/steamcmd  
  
ENTRYPOINT ["/opt/steamcmd/steamcmd.sh"]  

