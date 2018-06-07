FROM phusion/baseimage:0.9.11  
MAINTAINER Wilco Eliveld <wilcoeliveld@gmail.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set correct environment variables  
ENV HOME /root  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
# Install Dependencies  
RUN add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty
universe multiverse"  
RUN add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty-
updates universe multiverse"  
RUN apt-get update -q  
RUN apt-get install -qy libmono-cil-dev mediainfo sqlite3 wget unrar  
  
# Install NzbDrone  
RUN mkdir /opt/NzbDrone  
# http://update.nzbdrone.com/v2/develop/mono/NzbDrone.develop.tar.gz  
RUN wget -P /tmp/
http://update.nzbdrone.com/v2/develop/mono/NzbDrone.develop.tar.gz  
# RUN wget -P /tmp/
http://update.nzbdrone.com/v2/torrents/mono/NzbDrone.torrents.tar.gz  
RUN tar -C /opt/NzbDrone -xvf /tmp/NzbDrone.develop.tar.gz --strip-components
1  
  
# Directories  
VOLUME /config  
VOLUME /downloads  
VOLUME /tv  
VOLUME /torrent  
  
EXPOSE 8989  
# Add edge.sh to execute during container startup  
RUN mkdir -p /etc/my_init.d  
ADD edge.sh /etc/my_init.d/edge.sh  
RUN chmod +x /etc/my_init.d/edge.sh  
  
# Add nzbdrone to runit  
RUN mkdir /etc/service/nzbdrone  
ADD nzbdrone.sh /etc/service/nzbdrone/run  
RUN chmod +x /etc/service/nzbdrone/run  

