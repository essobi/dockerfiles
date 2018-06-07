FROM jameseckersall/alpine-base:3.5  
MAINTAINER James Eckersall <james.eckersall@gmail.com>  
  
RUN \  
echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
apk update && \  
apk add py2-pip deluge@testing && \  
pip install service_identity && \  
rm -rf /var/cache/apk/*  
  
COPY files /  
  
RUN \  
mkdir /config /torrents && \  
chmod -R 0777 /config /torrents && \  
chmod +x /hooks/supervisord-pre.d/*  
  
ENV \  
AUTOADD_LOCATION=/torrents/drop \  
CONFIG_DIR=/config \  
DAEMON_PORT=58846 \  
DELUGE_PASSWORD=deluge \  
DOWNLOAD_LOCATION=/torrents/.in_progress \  
GEOIP_DB=/config/GeoIP/GeoIP.dat \  
LISTEN_PORTS=6881,6891 \  
MOVE_COMPLETED_PATH=/torrents/completed \  
PLUGINS_LOCATION=/config/deluge/plugins \  
PYTHON_EGG_CACHE=/config/deluge/plugins \  
RANDOM_PORT=false \  
TORRENTFILES_LOCATION=/torrents/.torrents \  
TORRENTS_DIR=/torrents \  
UPNP=false \  
WEB_PORT=8112  
  
VOLUME ["/torrents", "/config"]  
  
EXPOSE 45682 8112/tcp 53160/tcp 53160/udp 58846/tcp  

