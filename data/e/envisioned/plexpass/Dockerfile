FROM lsiobase/xenial  
MAINTAINER Reg Stuser, envisioned  
  
# package version  
# global environment settings  
ENV DEBIAN_FRONTEND="noninteractive"  
ENV HOME="/config"  
# install packages  
RUN \  
apt-get update && \  
apt-get install -y \  
avahi-daemon \  
dbus \  
wget && \  
  
# install plex  
wget https://downloads.plex.tv/plex-media-
server/1.7.3.3937-70f781325/plexmediaserver_1.7.3.3937-70f781325_amd64.deb &&
\  
dpkg -i plexmediaserver_1.7.3.3937-70f781325_amd64.deb && \  
  
# cleanup  
apt-get clean && \  
rm -rf \  
/etc/default/plexmediaserver \  
/tmp/* \  
/var/lib/apt/lists/* \  
/var/tmp/*  
#  
# add local files  
COPY root/ /  
  
# ports and volumes  
EXPOSE 32400 32400/udp 32469 32469/udp 5353/udp 1900/udp  
VOLUME /config /transcode  

