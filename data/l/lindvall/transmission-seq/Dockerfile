FROM alpine:edge  
  
ARG TRANSMISSION_VER=2.92-seq  
ARG BUILD_CORES  
  
ENV UID=991 GID=991 \  
FLOOD_SECRET=supersecret  
  
RUN NB_CORES=${BUILD_CORES-`getconf _NPROCESSORS_CONF`} \  
&& BUILD_DEPS=" \  
build-base \  
patch \  
libtool \  
libevent-dev \  
automake \  
autoconf \  
cmake \  
wget \  
tar \  
xz \  
zlib-dev \  
cppunit-dev \  
libressl-dev \  
ncurses-dev \  
curl-dev \  
binutils" \  
&& apk -U upgrade && apk add \  
${BUILD_DEPS} \  
ca-certificates \  
curl \  
libressl \  
gzip \  
zip \  
zlib \  
unrar \  
s6 \  
su-exec \  
libevent \  
jq \  
&& cd /tmp && mkdir transmission \  
&& cd transmission && wget -qO-
https://github.com/Mikayex/transmission/archive/${TRANSMISSION_VER}.tar.gz |
tar xz --strip 1 \  
&& cd /tmp/transmission && cmake . && make -j ${NB_CORES} && make install \  
&& strip -s /usr/local/bin/transmission-daemon \  
&& apk del ${BUILD_DEPS} \  
&& rm -rf /var/cache/apk/* /tmp/*  
  
COPY s6.d /etc/s6.d  
COPY run.sh /usr/bin/  
COPY default-settings.json /default-settings.json  
  
RUN chmod +x /usr/bin/* /etc/s6.d/*/* /etc/s6.d/.s6-svscan/*  
  
VOLUME /home/transmission/.config/transmission-daemon
/home/transmission/Downloads  
  
EXPOSE 9091 51413 51413/udp  
  
LABEL description="BitTorrent client with WebUI front-end" \  
transmission="Transmission BiTorrent client v$TRANSMISSION_VER" \  
maintainer="lndvll <lndvll@targaryen.house>"  
  
CMD ["run.sh"]

