FROM ubuntu:16.04  
  
ARG GUACD_VERSION=0.9.14  
ARG BUILD_DATE  
ARG VCS_REF  
  
# Build-time metadata as defined at http://label-schema.org  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="guacd" \  
org.label-schema.description="guacd is the native server-side proxy used by
the Guacamole web application." \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/svengo/guacd" \  
org.label-schema.vendor="Sven Gottwald" \  
org.label-schema.version=$GUACD_VERSION \  
org.label-schema.schema-version="1.0"  
  
ENV \  
RUNTIME_DEPENDENCIES=" \  
ibfreerdp-client1.1 \  
libavcodec-ffmpeg56 \  
libavutil-ffmpeg54 \  
libcairo2 \  
libjpeg-turbo8 \  
libossp-uuid16 \  
libpango1.0 \  
libpng12-0 \  
libpulse0 \  
libssh2-1 \  
libssl1.0.0 \  
libswscale-ffmpeg3 \  
libtelnet2 \  
libvncserver1 \  
libvorbis0a \  
libwebp5 \  
ttf-dejavu" \  
BUILD_DEPENDENCIES=" \  
autoconf \  
automake \  
build-essential \  
libavcodec-dev \  
libavutil-dev \  
libcairo2-dev \  
libfreerdp-dev \  
libjpeg-turbo8-dev \  
libossp-uuid-dev \  
libpango1.0-dev \  
libpng12-dev \  
libpulse-dev \  
libssh2-1-dev \  
libssl-dev \  
libswscale-dev \  
libtelnet-dev \  
libtool \  
libvncserver-dev \  
libvorbis-dev \  
libwebp-dev \  
wget"  
  
WORKDIR /tmp  
RUN \  
apt-get update -y && \  
apt-get install -y $BUILD_DEPENDENCIES && \  
\  
wget --no-verbose --output-document="guacamole-server-${GUACD_VERSION}.tar.gz"
"http://apache.org/dyn/closer.cgi?action=download&filename=guacamole/${GUACD_VERSION}/source/guacamole-
server-${GUACD_VERSION}.tar.gz" && \  
wget --no-verbose
"https://www.apache.org/dist/guacamole/${GUACD_VERSION}/source/guacamole-
server-${GUACD_VERSION}.tar.gz.asc" && \  
gpg --keyserver ipv4.pool.sks-keyservers.net --recv-keys \  
0xE5E4518F && \  
gpg --verify "guacamole-server-${GUACD_VERSION}.tar.gz.asc" && \  
tar -zxf "guacamole-server-${GUACD_VERSION}.tar.gz" && \  
\  
cd guacamole-server-${GUACD_VERSION} && \  
autoreconf -fi && \  
./configure \  
\--silent \  
\--prefix=/usr && \  
make && \  
make install && \  
\  
apt-get remove --purge -y $BUILD_DEPENDENCIES $(apt-mark showauto) && \  
apt-get install --no-install-recommends -y $RUNTIME_DEPENDENCIES && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
  
EXPOSE 4822  
CMD [ "/usr/sbin/guacd", "-b", "0.0.0.0", "-f" ]  

