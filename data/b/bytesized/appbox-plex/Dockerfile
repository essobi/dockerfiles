FROM phusion/baseimage:0.9.21  
MAINTAINER Animazing  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LANG en_US.UTF-8  
ENV LC_ALL C.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV TERM xterm  
ENV HOME /config  
  
COPY run /etc/service/plex/run  
  
RUN apt-get -q update && \  
apt-get install -qy curl wget ca-certificates procps dbus avahi-daemon && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/* && \  
chmod +x /etc/service/plex/run && \  
echo /config > /etc/container_environment/HOME && \  
wget --quiet -O plex.deb https://downloads.plex.tv/plex-media-
server/1.8.1.4139-c789b3fbb/plexmediaserver_1.8.1.4139-c789b3fbb_amd64.deb &&
\  
dpkg -i plex.deb && \  
rm plex.deb  
  
VOLUME /config  
VOLUME /data  
VOLUME /flexdisk  
VOLUME /codecs  
  
EXPOSE 32400  
CMD ["/sbin/my_init"]  

