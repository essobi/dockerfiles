#Maintainer info@sinaptika.net  
#deluge http://deluge-torrent.org/  
#deluged image  
FROM sinaptika/libtorrent:1.0.11 as builder_libtorrent  
FROM alpine:3.7  
  
ENV \  
DELUGE_VERSION="1.3.15" \  
LIBTORRENT_VERSION="1.0.11" \  
LIBTORRENT_SO="8" \  
D_DIR="/opt/deluge" \  
D_USER="deluge" \  
D_GROUP="deluge" \  
D_D_PORT="58846" \  
D_D_INCOMING_PORT="50100" \  
TZ="Europe/London" \  
D_UID="1000" \  
D_GID="1000" \  
D_D_LOG_LEVEL="info"  
  
RUN \  
mkdir -p -v \  
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
  
COPY \  
scripts/deluged-pass.sh \  
scripts/docker-entrypoint.sh \  
/usr/bin/  
COPY \  
\--from=builder_libtorrent \  
/usr/lib/libtorrent-rasterbar.la \  
/usr/lib/libtorrent-rasterbar.so.${LIBTORRENT_SO}.0.0 \  
/usr/lib/  
COPY \  
\--from=builder_libtorrent \  
/usr/lib/python2.7/site-packages/libtorrent.so \  
/usr/lib/python2.7/site-
packages/python_libtorrent-${LIBTORRENT_VERSION}-py2.7.egg-info \  
/usr/lib/python2.7/site-packages/  
COPY \  
\--from=builder_libtorrent \  
/usr/lib/pkgconfig/libtorrent-rasterbar.pc \  
/usr/lib/pkgconfig/  
  
RUN \  
apk add --no-cache --virtual .runtime_libtorrent \  
boost-python boost-system libstdc++ python2 && \  
apk add --no-cache --virtual .system \  
tzdata su-exec tini pwgen p7zip && \  
apk add --no-cache --virtual .build_deluge \  
geoip openssl py2-pip intltool py2-mako && \  
apk add --no-cache --virtual .runtime_deluge \  
py-setuptools py2-openssl py-twisted py2-geoip py2-packaging py2-chardet && \  
pip install --no-cache-dir \  
pyxdg service_identity incremental constantly && \  
ln -s /usr/lib/libtorrent-rasterbar.so.${LIBTORRENT_SO}.0.0
/usr/lib/libtorrent-rasterbar.so && \  
ln -s /usr/lib/libtorrent-rasterbar.so.${LIBTORRENT_SO}.0.0
/usr/lib/libtorrent-rasterbar.so.${LIBTORRENT_SO} && \  
ldconfig -n -v /usr/lib && \  
wget -O- \  
https://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz
| \  
gunzip > /usr/share/GeoIP/GeoIP.dat && \  
wget -O- \  
http://download.deluge-torrent.org/source/deluge-${DELUGE_VERSION}.tar.gz | \  
tar xz && \  
cd /deluge-${DELUGE_VERSION} \  
python setup.py -q build && \  
python setup.py -q install && \  
cd / \  
rm -rf \  
/deluge-${DELUGE_VERSION} \  
/usr/lib/python2.7/site-packages/deluge-${DELUGE_VERSION}-py2.7.egg/share/* \  
/usr/lib/python2.7/site-
packages/deluge-${DELUGE_VERSION}-py2.7.egg/deluge/data/pixmaps/* \  
/usr/lib/python2.7/site-
packages/deluge-${DELUGE_VERSION}-py2.7.egg/deluge/ui/gtkui/* \  
/usr/lib/python2.7/site-
packages/deluge-${DELUGE_VERSION}-py2.7.egg/deluge/ui/i18n/* \  
/usr/lib/python2.7/site-
packages/deluge-${DELUGE_VERSION}-py2.7.egg/deluge/ui/web/* \  
/usr/bin/deluge /usr/bin/deluge-web /usr/bin/deluge-gtk && \  
apk del .build_deluge && \  
chmod +x \  
/usr/bin/deluged-pass.sh \  
/usr/bin/docker-entrypoint.sh  
  
WORKDIR \  
${D_DIR}/config  
  
RUN \  
/usr/bin/deluged \  
-c ${D_DIR}/config \  
-l ${D_DIR}/config/first_init.log \  
-L debug && \  
sleep 10 && \  
deluge-console \  
-c ${D_DIR}/config "config" && \  
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
${D_D_PORT} \  
${D_D_INCOMING_PORT} \  
${D_D_INCOMING_PORT}/udp  
  
VOLUME \  
${D_DIR}/config  
  
ENTRYPOINT \  
["/usr/bin/docker-entrypoint.sh"]  
  
LABEL \  
net.sinaptika.maintainer="info@sinaptika.net" \  
net.sinaptika.name="stable" \  
net.sinaptika.branch="master" \  
net.sinaptika.from="alpine:3.7" \  
c_software_name="Deluge Daemon" \  
c_software_url="http://deluge-torrent.org/" \  
image.version="0.9" \  
date.version="4.2.2018" \  
web_interface="true" \  
web_interface_port=${D_D_PORT} \  
exposed_ports=${D_D_PORT},${D_D_INCOMING_PORT},${D_D_INCOMING_PORT}/udp \  
docker_volumes=${D_DIR}

