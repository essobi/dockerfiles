# vim: set expandtab ts=2 :  
FROM ubuntu:trusty  
  
MAINTAINER sebastien@gregoire.email  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y \  
supervisor transmission-daemon  
  
ADD config/settings.json /etc/transmission-daemon/settings.json  
ADD config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ADD start.sh /start.sh  
  
VOLUME /data/download  
VOLUME /data/watchdir  
  
EXPOSE 9091  
EXPOSE 51413  
CMD ["/start.sh"]  

