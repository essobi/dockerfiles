FROM ubuntu  
  
MAINTAINER Josh Schueths <jschueths@gmail.com>  
  
VOLUME ["/var/lib/transmission-daemon/info/torrents"]  
VOLUME ["/var/lib/transmission-daemon/info/resume"]  
VOLUME ["/var/lib/transmission-daemon/downloads"]  
  
ENV TRANSMISSION_USER="transmission"  
ENV TRANSMISSION_PASSWORD="transmission"  
EXPOSE 9091  
EXPOSE 51413  
RUN apt-get update  
RUN apt-get install -y transmission-daemon  
  
ADD settings.json /var/lib/transmission-daemon/info/settings.json  
ADD docker-entrypoint.sh /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["-f", "-g", "/var/lib/transmission-daemon/info"]  
  

