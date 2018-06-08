FROM lsiobase/xenial  
MAINTAINER Stian Larsen, sparklyballs  
  
  
# global environment settings  
ENV DEBIAN_FRONTEND="noninteractive" \  
PLEX_DOWNLOAD="https://downloads.plex.tv/plex-media-server" \  
PLEX_INSTALL="https://plex.tv/downloads/latest/1?channel=8&build=linux-
ubuntu-x86_64&distro=ubuntu" \  
PLEX_MEDIA_SERVER_APPLICATION_SUPPORT_DIR="/config/Library/Application
Support" \  
PLEX_MEDIA_SERVER_HOME="/usr/lib/plexmediaserver" \  
PLEX_MEDIA_SERVER_INFO_DEVICE=docker \  
PLEX_MEDIA_SERVER_MAX_PLUGIN_PROCS="6" \  
PLEX_MEDIA_SERVER_USER=abc  
  
# install packages  
RUN \  
apt-get update && \  
apt-get install -y \  
avahi-daemon \  
dbus \  
unrar \  
python3 \  
git \  
build-essential \  
libargtable2-dev \  
autoconf \  
libtool-bin \  
ffmpeg \  
libsdl1.2-dev \  
libavutil-dev \  
libavformat-dev \  
libavcodec-dev \  
wget && \  
# install plex  
curl -o \  
/tmp/plexmediaserver.deb -L \  
"${PLEX_INSTALL}" && \  
dpkg -i /tmp/plexmediaserver.deb && \  
# change abc home folder to fix plex hanging at runtime with usermod  
usermod -d /app abc && \  
# Clone Comskip  
cd /opt && \  
git clone git://github.com/erikkaashoek/Comskip && \  
cd Comskip && \  
./autogen.sh && \  
./configure && \  
make && \  
  
# Clone PlexComskip  
cd /opt && \  
git clone https://github.com/ekim1337/PlexComskip.git && \  
chmod -R 777 /opt/ /tmp/ /root/ && \  
touch /var/log/PlexComskip.log && \  
chmod 777 /var/log/PlexComskip.log && \  
# cleanup  
apt-get clean && \  
rm -rf \  
/var/lib/apt/lists/* \  
/etc/default/plexmediaserver \  
/tmp/* \  
/var/lib/apt/lists/* \  
/var/tmp/*  
  
ADD ./PlexComskip.conf /opt/PlexComskip/PlexComskip.conf  
  
  
# add local files  
COPY root/ /  
  
# ports and volumes  
EXPOSE 32400 32400/udp 32469 32469/udp 5353/udp 1900/udp  
VOLUME /config /transcode  

