FROM ubuntu:14.04  
MAINTAINER Jérémy SEBAN <jeremy@seban.eu>  
  
# Setting plex verion  
ENV PLEXVERSION 1.8.1.4139-c789b3fbb  
  
# Installing plex  
RUN apt-get -qq update  
RUN apt-get -qq install -y wget  
RUN locale-gen en_US.UTF-8  
RUN wget --quiet https://downloads.plex.tv/plex-media-
server/${PLEXVERSION}/plexmediaserver_${PLEXVERSION}_amd64.deb -O plex.deb  
RUN dpkg -i plex.deb  
RUN rm plex.deb  
  
# Setting /etc/plex as a volume since it's where it will store its
configuration  
VOLUME ["/etc/plex"]  
  
ENV PLEX_MEDIA_SERVER_APPLICATION_SUPPORT_DIR /etc/plex  
ENV PLEX_MEDIA_SERVER_HOME /usr/lib/plexmediaserver  
ENV PLEX_MEDIA_SERVER_MAX_PLUGIN_PROCS 6  
ENV PLEX_MEDIA_SERVER_TMPDIR /tmp  
ENV LD_LIBRARY_PATH /usr/lib/plexmediaserver  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
# Exposing Plex Web UI  
EXPOSE 32400  
# Plex start command  
CMD ["/usr/lib/plexmediaserver/Plex Media Server"]  

