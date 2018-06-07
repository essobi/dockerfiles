FROM debian:latest  
MAINTAINER Aurelien RICHAUD <aurelien.richaud@cenconnect.com>  
  
# Installation de HeartBeat  
RUN apt-get update && apt-get install -y heartbeat pacemaker  
  
# Script d'initialisation  
COPY init.sh /usr/local/bin/init.sh  
RUN chmod 0755 /usr/local/bin/init.sh  
  
CMD ["bash", "-c", "/usr/local/bin/init.sh"]

