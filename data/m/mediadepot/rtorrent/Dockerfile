FROM lsiobase/alpine:3.7 as builder  
###############################################################################  
# Build Image  
# using modified version of https://github.com/romancin/rutorrent-flood-
docker/  
###############################################################################  
  
# set version label  
ARG BUILD_DATE  
ARG VERSION  
ARG BUILD_CORES  
  
# package version  
ARG RTORRENT_VER="0.9.6"  
ARG LIBTORRENT_VER="0.13.6"  
ARG CURL_VER="7.57.0"  
ARG FLOOD_VER="1.0.0"  
  
# set env  
ENV PKG_CONFIG_PATH=/usr/local/lib/pkgconfig  
ENV LD_LIBRARY_PATH=/usr/local/lib  
  
RUN NB_CORES=${BUILD_CORES-`getconf _NPROCESSORS_CONF`} && \  
apk add --no-cache \  
ca-certificates \  
libressl \  
nodejs \  
nodejs-npm \  
python \  
tar \  
unrar \  
unzip \  
wget \  
zip \  
zlib-dev \  
zlib && \  
  
# install build packages  
apk add --no-cache --virtual=build-dependencies \  
autoconf \  
automake \  
binutils \  
build-base \  
cppunit-dev \  
curl-dev \  
gcc \  
git \  
g++ \  
libressl-dev \  
libtool \  
linux-headers \  
make \  
ncurses-dev \  
subversion && \  
  
# compile curl to fix ssl for rtorrent  
cd /tmp && \  
mkdir curl && \  
cd curl && \  
wget -qO- https://curl.haxx.se/download/curl-${CURL_VER}.tar.gz | tar xz
--strip 1 && \  
./configure --disable-shared --with-ssl && make -j ${NB_CORES} && \  
make install && make install DESTDIR=/tmp/artifacts && \  
ldconfig /usr/bin && ldconfig /usr/lib && \  
  
# compile xmlrpc-c  
cd /tmp && \  
mkdir xmlrpc-c && \  
cd /tmp/xmlrpc-c && \  
wget -qO- https://github.com/mirror/xmlrpc-c/archive/master.tar.gz | tar xz
--strip-components=2 xmlrpc-c-master/stable && \  
./configure --with-libwww-ssl --disable-wininet-client --disable-curl-client
--disable-libwww-client --disable-abyss-server --disable-cgi-server && make -j
${NB_CORES} && \  
make install && make install DESTDIR=/tmp/artifacts && \  
  
  
# compile libtorrent  
apk add -X http://dl-cdn.alpinelinux.org/alpine/v3.6/main -U cppunit-
dev==1.13.2-r1 cppunit==1.13.2-r1 && \  
cd /tmp && \  
mkdir libtorrent && \  
cd libtorrent && \  
wget -qO-
https://github.com/rakshasa/libtorrent/archive/${LIBTORRENT_VER}.tar.gz | tar
xz --strip 1 && \  
./autogen.sh && ./configure --enable-static --disable-shared && make -j
${NB_CORES} && \  
make install && make install DESTDIR=/tmp/artifacts && \  
  
# compile rtorrent  
cd /tmp && \  
mkdir rtorrent && \  
cd rtorrent && \  
wget -qO- https://github.com/rakshasa/rtorrent/archive/${RTORRENT_VER}.tar.gz
| tar xz --strip 1 && \  
./autogen.sh && ./configure --with-xmlrpc-c && make -j ${NB_CORES} && \  
make install && make install DESTDIR=/tmp/artifacts && \  
  
# ensure successful build  
rtorrent -h && \  
  
# install flood webui  
mkdir /usr/flood && \  
cd /usr/flood && \  
git clone https://github.com/jfurrow/flood . && \  
cp config.template.js config.js && \  
npm install --build-from-source=bcrypt && \  
npm run build && \  
rm config.js && \  
  
# cleanup  
apk del --purge build-dependencies && \  
apk del -X http://dl-cdn.alpinelinux.org/alpine/v3.6/main cppunit-dev  
  
###############################################################################  
# Runtime Image  
###############################################################################  
  
FROM alpine as runtime  
MAINTAINER Jason Kulatunga <jason@thesparktree.com>  
  
# root filesystem  
RUN mkdir -p /etc/cont-finish.d \  
/etc/cont-init.d \  
/etc/fix-attrs.d \  
/etc/services.d  
  
# copy over distribution config.sh file. Configures container user & group
with customizable PID & GID  
WORKDIR /srv/  
  
RUN apk --update --no-cache add \  
curl && \  
mkdir ~/.ssh && \  
curl -L -s https://github.com/just-
containers/s6-overlay/releases/download/v1.18.1.5/s6-overlay-amd64.tar.gz \  
| tar xvzf - -C /  
  
  
  
### END OF MEDIADEPOT BASE  
  
  
# set env  
ENV PKG_CONFIG_PATH=/usr/local/lib/pkgconfig  
ENV LD_LIBRARY_PATH=/usr/local/lib  
  
#Create rtorrent folder structure & set as volumes  
RUN mkdir -p /srv/flood/app && \  
mkdir -p /srv/rtorrent/config && \  
mkdir -p /srv/rtorrent/data && \  
  
# create rtorrent storage structure  
mkdir -p /mnt/blackhole && \  
mkdir -p /mnt/processing && \  
mkdir -p /mnt/downloads  
  
RUN apk add --no-cache \  
bash \  
ca-certificates \  
screen \  
libressl \  
nodejs \  
nodejs-npm \  
python \  
tar \  
unrar \  
unzip \  
wget \  
zip \  
zlib-dev \  
zlib && \  
rm -rf /var/cache/apk/* /tmp/* && \  
cd /srv/rtorrent/data/ && \  
curl -O -L https://raw.githubusercontent.com/rakshasa/rtorrent-
vagrant/master/scripts/xmlrpc2scgi.py  
# test with:  
  
# Copy the build artifacts from the builder stage.  
COPY --from=builder /tmp/artifacts /  
COPY --from=builder /usr/flood /srv/flood/app  
# add local files  
COPY rootfs/ /  
  
# ports and volumes  
VOLUME ["/srv/rtorrent/config", "/srv/rtorrent/data"]  
EXPOSE 8081  
EXPOSE 5000  
EXPOSE 6880-6891  
  
CMD ["/init"]  
  

