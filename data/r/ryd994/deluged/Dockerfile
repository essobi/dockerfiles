FROM alpine:edge  
MAINTAINER Yidong Ren <docker@yidong.im>  
ARG DELUGE_USER=deluge  
ARG BUILD_DIR=/build/  
RUN VERSION=`wget -O - http://download.deluge-torrent.org/version` &&\  
apk add \--no-cache --repository http://dl-
cdn.alpinelinux.org/alpine/edge/testing/ python2 py-setuptools libtorrent-
rasterbar py-chardet py-xdg py-twisted py-openssl py-service_identity ca-
certificates py-certifi py-setproctitle py-rencode py-markupsafe py-mako &&\  
apk add \--no-cache --virtual build-dependencies py2-pip bash &&\  
pip install attrs twisted pyOpenSSL slimit &&\  
mkdir ${BUILD_DIR} && cd ${BUILD_DIR} &&\  
wget -O - http://download.deluge-torrent.org/source/deluge-${VERSION}.tar.xz |
tar xJ &&\  
cd deluge-${VERSION}/ &&\  
sed -i 's/storage_mode = lt.storage_mode_t(1)/storage_mode =
lt.storage_mode_t(0)/' deluge/core/torrentmanager.py &&\  
python setup.py build install &&\  
adduser -D ${DELUGE_USER} &&\  
cd / && rm -rf ${BUILD_DIR} &&\  
apk del build-dependencies  
EXPOSE 58846  
USER ${DELUGE_USER}  
VOLUME /home/${DELUGE_USER}/  
ENTRYPOINT ["/usr/bin/deluged", "--do-not-daemonize"]  

