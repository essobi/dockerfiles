FROM debian:jessie  
MAINTAINER Chris Staley me@unixtime.site  
  
ENV DELUGE_VERSION 1.3.12  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install -y python python-twisted python-twisted-web
python3-openssl python3-openssl python-xdg python-chardet  
RUN apt-get install -y python-setproctitle python-gtk2 python-rsvg python-
notify python-pygame python-appindicator python-mako python-libtorrent  
RUN apt-get install -y libtorrent-rasterbar7 gettext intltool geoip-database
xdg-utils wget  
  
RUN wget http://download.deluge-
torrent.org/source/deluge-$DELUGE_VERSION.tar.gz -O /tmp/deluge.tgz  
RUN tar xzf /tmp/deluge.tgz -C /tmp  
RUN cd /tmp/deluge* && python setup.py build && python setup.py install
--install-layout=deb  
RUN apt-get -y clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD run.sh /run.sh  
ADD core.conf /core.conf.def  
  
VOLUME ["/config", "/data/downloads", "/data/auto-add", "/data/downloads-inc"]  
  
EXPOSE 62958 62958/udp 58846  
ENTRYPOINT ["/bin/bash", "/run.sh"]

