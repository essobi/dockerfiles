FROM debian:stretch-slim  
  
ARG GUACAMOLE_VERSION="0.9.14"  
ENV HOME=/config  
  
COPY ./docker-entrypoint.sh /docker-entrypoint.sh  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -qq && \  
DEBIAN_FRONTEND=noninteractive apt-get install -qy \  
ca-certificates \  
gcc \  
make \  
libc6-dev \  
libcairo2-dev \  
libpng-dev \  
libossp-uuid-dev \  
libvncserver-dev \  
libfreerdp-dev \  
libssl1.0-dev \  
libpango1.0-dev \  
libwebp-dev \  
libssh2-1-dev \  
libtelnet-dev \  
libpulse-dev \  
libvorbis-dev \  
wget && \  
DEBIAN_FRONTEND=noninteractive apt-get install -qy \  
gir1.2-pango-1.0 \  
gosu \  
libcairo2 \  
libpango-1.0-0 \  
libwebp6 \  
libvncserver1 \  
libvncclient1 \  
libvorbis0a \  
libtelnet2 \  
libossp-uuid16 \  
libjpeg62-turbo \  
libssh2-1 \  
libfreerdp-client1.1 \  
libfreerdp-cache1.1 \  
libfreerdp-gdi1.1 \  
libfreerdp-rail1.1 \  
libfreerdp-plugins-standard \  
libxfreerdp-client1.1 \  
libpulse0 \  
xfonts-terminus && \  
wget -qO /tmp/guacamole-server.tar.gz
"http://apache.org/dyn/closer.cgi?action=download&filename=guacamole/${GUACAMOLE_VERSION}/source/guacamole-
server-${GUACAMOLE_VERSION}.tar.gz" && \  
tar xzf /tmp/guacamole-server.tar.gz -C /tmp && \  
cd /tmp/guacamole-server-${GUACAMOLE_VERSION} && \  
./configure --prefix=/usr --sbindir=/usr/bin && \  
make -j$(nproc) && \  
make install && \  
ldconfig && \  
ln -s /usr/lib/freerdp/guacdr-client.so /usr/lib/x86_64-linux-
gnu/freerdp/guacdr-client.so && \  
ln -s /usr/lib/freerdp/guacsnd-client.so /usr/lib/x86_64-linux-
gnu/freerdp/guacsnd-client.so && \  
DEBIAN_FRONTEND=noninteractive apt-get purge -qq \  
gcc \  
make \  
libc6-dev \  
libcairo2-dev \  
libpng-dev \  
libossp-uuid-dev \  
libvncserver-dev \  
libfreerdp-dev \  
libssl-dev \  
libpango1.0-dev \  
libwebp-dev \  
libssh2-1-dev \  
libtelnet-dev \  
libpulse-dev \  
libvorbis-dev \  
wget && \  
DEBIAN_FRONTEND=noninteractive apt-get -y autoremove --purge && \  
DEBIAN_FRONTEND=noninteractive apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
useradd -r -u 911 -U -d /config -s /bin/false abc && \  
usermod -G users abc && \  
chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

