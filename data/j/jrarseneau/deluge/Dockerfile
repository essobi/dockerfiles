FROM ubuntu:14.04  
MAINTAINER J.R. Arseneau <http://github.com/jrarseneau>  
  
ENV LANG en_US.UTF-8  
RUN locale-gen $LANG  
  
# To get rid of error messages like "debconf: unable to initialize frontend:
Dialog":  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty multiverse" >>
/etc/apt/sources.list  
  
# Update our image  
RUN apt-get -q update  
RUN apt-get -qy --force-yes dist-upgrade  
  
# Install Deluge  
RUN apt-get install -qy deluged deluge-web  
  
# Torrent port  
EXPOSE 53160  
EXPOSE 53160/udp  
# WebUI  
EXPOSE 8112  
# Daemon  
EXPOSE 58846  
VOLUME /volumes/config  
VOLUME /volumes/downloads  
VOLUME /volumes/media  
  
ADD start.sh /  
RUN chmod +x /start.sh  
  
ENTRYPOINT ["/start.sh"]  

