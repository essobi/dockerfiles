FROM debian:jessie  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
ca-certificates \  
libcurl4-openssl-dev \  
libssl-dev \  
jq \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV LIBEVENT_VERSION 2.0.18-stable  
ENV TRANSMISSION_VERSION 2.90  
  
RUN buildDeps=' \  
curl \  
build-essential \  
intltool \  
pkg-config \  
' \  
&& set -x \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $buildDeps \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /build \  
&& curl -SL
"https://github.com/downloads/libevent/libevent/libevent-$LIBEVENT_VERSION.tar.gz"
\  
| tar -xzC /build/ \  
&& cd /build/libevent-$LIBEVENT_VERSION \  
&& CFLAGS="-Os -march=native" ./configure \  
&& make -j"$(nproc)" \  
&& make install \  
&& rm -rf /build \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get purge -y --auto-remove $buildDeps  
  
RUN buildDeps=' \  
curl \  
build-essential \  
intltool \  
pkg-config \  
' \  
&& set -x \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $buildDeps \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /build \  
&& curl -SL "http://download-
origin.transmissionbt.com/files/transmission-$TRANSMISSION_VERSION.tar.xz" \  
| tar -xJC /build/ \  
&& cd /build/transmission-$TRANSMISSION_VERSION \  
&& CFLAGS="-Os -march=native" ./configure \  
&& make -j"$(nproc)" \  
&& make install \  
&& rm -rf /build \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get purge -y --auto-remove $buildDeps  
  
RUN buildDeps=' \  
curl \  
' \  
&& set -x \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $buildDeps \  
&& curl -SL "https://github.com/hdorio/docker-
transmission/blob/master/gosu?raw=true" > /bin/gosu \  
&& chmod +x /bin/gosu \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get purge -y --auto-remove $buildDeps  
  
RUN groupadd -r transmission && useradd -r -g transmission transmission  
  
COPY default-settings.json /default-settings.json  
COPY entrypoint.sh /entrypoint.sh  
  
VOLUME /home/transmission/.config/transmission-daemon  
VOLUME /home/transmission/Downloads  
EXPOSE 9091  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["transmission-daemon", "-f"]  

