FROM ubuntu:16.04  
MAINTAINER Tim Haak <tim@haak.co>  
  
ENV DEBIAN_FRONTEND="noninteractive" \  
TERM="xterm"  
  
ENV PLEX_PPA_DIST="wheezy" \  
PLEX_PASS_PPA="plexpass"  
  
ARG PLEX_VERSION='plexpass'  
  
RUN echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup &&\  
echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache && \  
apt-get -q update && \  
apt-get -qy dist-upgrade && \  
apt-get install -qy \  
iproute2 \  
ca-certificates \  
openssl \  
xmlstarlet \  
curl \  
sudo \  
&& \  
echo "deb http://shell.ninthgate.se/packages/debian ${PLEX_VERSION} main" >
/etc/apt/sources.list.d/plexmediaserver.list && \  
curl http://shell.ninthgate.se/packages/shell.ninthgate.se.gpg.key | apt-key
add \- && \  
apt-get -q update && \  
apt-get install -qy plexmediaserver && \  
apt-get -y autoremove && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
  
VOLUME ["/config","/data", "/media"]  
  
ENV RUN_AS_ROOT="true" \  
CHANGE_DIR_RIGHTS="false" \  
CHANGE_CONFIG_DIR_OWNERSHIP="true" \  
HOME="/config" \  
PLEX_DISABLE_SECURITY=0  
  
EXPOSE 32400  
  
ADD ./static/Preferences.xml /opt/Preferences.xml  
ADD ./static/start.sh /opt/start.sh  
  
CMD ["/opt/start.sh"]  

