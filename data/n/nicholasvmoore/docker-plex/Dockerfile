# Plex  
#  
# Version: 0.0.8  
FROM fedora:21  
MAINTAINER Nicholas Moore  
  
VOLUME /var/lib/plexmediaserver/  
VOLUME /media  
  
ADD ./start.sh /start.sh  
  
RUN cp /usr/share/zoneinfo/US/Pacific /etc/localtime;\  
rpm -ivh --force https://downloads.plex.tv/plex-media-
server/0.9.12.11.1406-8403350/plexmediaserver-0.9.12.11.1406-8403350.x86_64.rpm  
EXPOSE 32400  
ENTRYPOINT ["/start.sh"]  

