FROM ubuntu:18.04  
RUN apt-get -qq update  
RUN apt-get -qqy --force-yes dist-upgrade  
RUN apt-get install -qqy --force-yes wget avahi-daemon avahi-utils locales
udev  
  
RUN locale-gen en_US en_US.UTF-8  
  
VOLUME /config  
VOLUME /data  
  
ADD ./start.sh /start.sh  
RUN chmod u+x /start.sh  
  
EXPOSE 32400  
ENV PLEX_VERSION 1.13.0.5023-31d3c0c65  
RUN wget https://downloads.plexapp.com/plex-media-
server/${PLEX_VERSION}/plexmediaserver_${PLEX_VERSION}_amd64.deb  
RUN dpkg -i plexmediaserver_${PLEX_VERSION}_amd64.deb  
  
ENTRYPOINT ["/start.sh"]  
  

