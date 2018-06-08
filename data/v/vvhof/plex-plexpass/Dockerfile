FROM timhaak/plex:latest  
MAINTAINER Tim Haak and vvhof <contact us on github>  
#Thanks to https://github.com/bydavy/docker-plex/blob/master/Dockerfile and
https://github.com/aostanin/docker-plex/blob/master/Dockerfile  
ENV DEBIAN_FRONTEND noninteractive  
  
# Add the plexpass channel, update and reduce image size afterwards  
RUN echo "deb http://shell.ninthgate.se/packages/debian plexpass main" >
/etc/apt/sources.list.d/plexmediaserver.list && \  
apt-get -q update && \  
apt-get upgrade -qy --force-yes && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
  
VOLUME /config  
VOLUME /data  
  
EXPOSE 32400  
CMD ["/start.sh"]  

