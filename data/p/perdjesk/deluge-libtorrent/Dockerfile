FROM debian:stable  
  
# General dependencies to be present in final image  
RUN apt-get update && apt-get install --no-install-recommends -y \  
curl python python-twisted python-openssl python-setuptools intltool \  
python-xdg python-chardet geoip-database python-libtorrent python-notify \  
python-pygame python-glade2 librsvg2-common xdg-utils python-mako \  
supervisor && \  
apt-get clean  
  
# Libtorrent. Deps, compilation, installation and cleaning  
RUN apt-get update && apt-get install --no-install-recommends -y libboost-all-
dev make g++ libssl-dev && \  
mkdir -p /tmp/libtorrent && \  
cd /tmp/libtorrent && \  
curl -SL
http://sourceforge.net/projects/libtorrent/files/libtorrent/libtorrent-
rasterbar-1.0.4.tar.gz/download -o release.tar.gz && \  
echo "a2029f10e7ae9f8f1885c6cd308b737482c1d737 release.tar.gz" | sha1sum -c \-
&& \  
echo "1f567823133b1493b9717afc8334eed691bf0ab452d4a2e0f644989f13ce9db0
release.tar.gz" | sha256sum -c \- && \  
tar -zxvf release.tar.gz && \  
cd libtorrent* && \  
./configure --enable-python-binding -enable-debug=no && \  
make -j2 install && \  
ldconfig && \  
rm -fr /tmp/libtorrent && \  
apt-get purge -y libboost-all-dev make g++ && \  
apt-get autoremove -y && \  
apt-get clean  
  
# Deluge. Compilation, installation and cleaning  
RUN mkdir -p /tmp/deluge && \  
cd /tmp/deluge && \  
curl -SL http://download.deluge-torrent.org/source/deluge-1.3.11.tar.gz -o
release.tar.gz && \  
echo "3129f8a4b857028917626de56c673e409920a3a8 release.tar.gz" | sha1sum -c \-
&& \  
echo "80b0a2a3460d52a5f53df26a9ce314e3e792f2e3f45b7c389140fd830bdee1b0
release.tar.gz" | sha256sum -c \- && \  
tar -zxvf release.tar.gz && \  
cd deluge* && \  
python setup.py build && \  
python setup.py install && \  
rm -fr /tmp/deluge  
  
# Deluge WebClient  
EXPOSE 8112  
  
# Deluged  
EXPOSE 58846  
  
# BitTorrent incoming  
EXPOSE 6881  
EXPOSE 6881/udp  
  
# Volumes  
VOLUME /config  
VOLUME /log  
VOLUME /data  
  
# add the deluge:deluge user:group  
RUN adduser --system -shell "/bin/bash" \--disabled-password --group --home
/var/lib/deluge deluge  
  
# import the supervisor configuration  
ADD *.conf /etc/supervisor/conf.d/  
  
# setup command script file  
ADD command.sh /opt/command.sh  
RUN chmod +x /opt/command.sh  
  
CMD ["/opt/command.sh"]  

