#Maintainer info@sinaptika.net  
#deluge http://deluge-torrent.org/  
#deluge image  
FROM sinaptika/libtorrent:1.1.3 as builder_libtorrent  
  
FROM alpine:3.7  
#Enviroment variables for building the image.  
#Enviroment variables for running the container.  
#Pass at docker create or docker run (-e VARIABLE=value).  
ENV \  
DELUGE_VERSION="2.0b1" \  
LIBTORRENT_VERSION="1.1.3" \  
LIBTORRENT_SO="9" \  
D_DIR="/opt/deluge" \  
D_USER="deluge" \  
D_GROUP="deluge" \  
D_W_PORT="8112" \  
D_D_PORT="58846" \  
D_D_INCOMING_PORT="50100" \  
TZ="Europe/London" \  
D_UID="1000" \  
D_GID="1000" \  
D_D_UMASK="022" \  
D_D_LOG_LEVEL="info" \  
D_W_LOG_LEVEL="info"  
#Create directory structure and add user:group.  
RUN \  
mkdir -p \  
${D_DIR} \  
${D_DIR}/config \  
${D_DIR}/complete \  
${D_DIR}/downloads && \  
addgroup -g \  
${D_GID} -S ${D_GROUP} && \  
adduser \  
-h ${D_DIR} \  
-g "Deluge system user" \  
-G ${D_GROUP} \  
-S -D \  
-u ${D_UID} ${D_USER}  
  
  
#Copy entrypoint and deluged-pass.sh  
COPY \  
scripts/deluged-pass.sh \  
scripts/docker-entrypoint.sh \  
/usr/bin/  
#Copy supervisor configuration file.  
COPY \  
scripts/supervisord.conf \  
${D_DIR}/config/  
#Copy libtorrent-rasterbar from sinaptika/libtorrent  
COPY \  
\--from=builder_libtorrent \  
/usr/lib/libtorrent-rasterbar.la \  
/usr/lib/libtorrent-rasterbar.so.${LIBTORRENT_SO}.0.0 \  
/usr/lib/  
#Copy python bindings from sinaptika/libtorrent  
COPY \  
\--from=builder_libtorrent \  
/usr/lib/python2.7/site-packages/libtorrent.so \  
/usr/lib/python2.7/site-
packages/python_libtorrent-${LIBTORRENT_VERSION}-py2.7.egg-info \  
/usr/lib/python2.7/site-packages/  
#Copy pkgconfig  
COPY \  
\--from=builder_libtorrent \  
/usr/lib/pkgconfig/libtorrent-rasterbar.pc \  
/usr/lib/pkgconfig/  
#Libtorrent  
#deluge  
#automat package needed for deluge-web only  
#Cleanup and chmod for entrypoint and pwgen script.  
RUN \  
cd && \  
apk add --no-cache --virtual .runtime_libtorrent \  
boost-python boost-system libstdc++ python2 && \  
ln -s /usr/lib/libtorrent-rasterbar.so.${LIBTORRENT_SO}.0.0
/usr/lib/libtorrent-rasterbar.so && \  
ln -s /usr/lib/libtorrent-rasterbar.so.${LIBTORRENT_SO}.0.0
/usr/lib/libtorrent-rasterbar.so.${LIBTORRENT_SO} && \  
ldconfig -n -v /usr/lib && \  
cd && \  
apk add --no-cache --virtual .system \  
tzdata supervisor pwgen p7zip && \  
apk add --no-cache --virtual .build_deluge \  
git gettext geoip openssl py2-pip intltool && \  
apk add --no-cache --virtual .runtime_deluge \  
py-setuptools py2-mako py2-openssl py-twisted py2-geoip && \  
pip install --no-cache-dir \  
pyxdg service_identity incremental constantly packaging automat slimit chardet
&& \  
wget \  
https://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz
-O \  
/tmp/GeoIP.dat.gz && gunzip /tmp/GeoIP.dat.gz && \  
mv \  
/tmp/GeoIP.dat /usr/share/GeoIP && \  
git clone https://github.com/deluge-torrent/deluge.git && \  
cd deluge && \  
git checkout tags/deluge-${DELUGE_VERSION} && \  
python setup.py -q build && \  
python setup.py -q install && \  
rm -rf \  
/usr/lib/python2.7/site-packages/deluge-${DELUGE_VERSION}-py2.7.egg/share/* \  
/usr/lib/python2.7/site-
packages/deluge-${DELUGE_VERSION}-py2.7.egg/deluge/data/pixmaps/* \  
/usr/lib/python2.7/site-
packages/deluge-${DELUGE_VERSION}-py2.7.egg/deluge/ui/gtkui/* \  
/usr/lib/python2.7/site-
packages/deluge-${DELUGE_VERSION}-py2.7.egg/deluge/ui/i18n/* \  
/usr/bin/deluge /usr/bin/deluge-gtk && \  
apk del .build_deluge && \  
cd && \  
rm -rf \  
/root/* && \  
chmod +x \  
/usr/bin/deluged-pass.sh \  
/usr/bin/docker-entrypoint.sh  
#Deluged first run  
#Deluged configuration  
#Using status instead of config to print defaults in 2.0  
RUN \  
/usr/bin/deluge-web \  
-f -c ${D_DIR}/config -l ${D_DIR}/config/deluge-web-init.log -L debug && \  
sleep 10 && \  
pkill -15 python && \  
/usr/bin/deluged \  
-c ${D_DIR}/config \  
-l ${D_DIR}/config/deluged-init.log \  
-L debug && \  
sleep 10 && \  
deluge-console \  
-c ${D_DIR}/config "status" && \  
deluge-console \  
-c ${D_DIR}/config "config -s allow_remote true" && \  
deluge-console \  
-c ${D_DIR}/config "config -s move_completed_path ${D_DIR}/complete" && \  
deluge-console \  
-c ${D_DIR}/config "config -s download_location ${D_DIR}/downloads" && \  
deluge-console \  
-c ${D_DIR}/config "config -s daemon_port ${D_D_PORT}" && \  
deluge-console \  
-c ${D_DIR}/config "config -s random_port false" && \  
deluge-console \  
-c ${D_DIR}/config "config -s listen_ports (${D_D_INCOMING_PORT},${D_D_INCOMING_PORT})" && \  
deluge-console \  
-c ${D_DIR}/config "halt" && \  
rm -rf \  
${D_DIR}/config/ssl/* && \  
chown -R \  
${D_USER}:${D_GROUP} \  
${D_DIR}  
  
EXPOSE \  
${D_W_PORT} \  
${D_D_PORT} \  
${D_D_INCOMING_PORT} \  
${D_D_INCOMING_PORT}/udp  
  
VOLUME \  
${D_DIR}/config  
  
ENTRYPOINT \  
["/usr/bin/docker-entrypoint.sh"]  
  
LABEL \  
net.sinaptika.maintainer="info@sinaptika.net" \  
net.sinaptika.name="deluge" \  
net.sinaptika.branch="master" \  
net.sinaptika.from="alpine:3.6" \  
c_software_name="Deluge" \  
c_software_url="http://deluge-torrent.org/" \  
image.version="dev" \  
date.version="29.12.2017" \  
web_interface="true" \  
web_interface_port=${D_W_PORT} \  
exposed_ports=${D_W_PORT},${D_D_PORT},${D_D_INCOMING_PORT},${D_D_INCOMING_PORT}/udp
\  
docker_volumes=${D_DIR}  

