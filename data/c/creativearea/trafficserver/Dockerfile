FROM ubuntu:14.04  
MAINTAINER CREATIVE AREA  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -q update && apt-get install -y ca-certificates curl --no-install-
recommends && rm -r /var/lib/apt/lists/*  
  
ENV TS_VERSION 6.1.1  
ENV TS_DOWNLOAD_URL
http://apache.mirrors.ovh.net/ftp.apache.org/dist/trafficserver/trafficserver-$TS_VERSION.tar.bz2  
  
RUN buildDeps="libssl-dev tcl-dev libexpat1-dev libpcre3-dev libtool libaio-
dev libcap-dev bison flex dpkg-dev pkg-config libgeoip-dev liblua5.1-0-dev dh-
autoreconf libboost-dev python-sphinx libhwloc-dev libmysqlclient-dev
libxml2-dev libunwind8-dev" \  
&& set -x \  
&& apt-get update && apt-get install -y $buildDeps \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /opt/src/ts \  
&& curl -sSL "$TS_DOWNLOAD_URL" -o ts.tar.bz2 \  
&& tar -xjf ts.tar.bz2 -C /opt/src/ts \--strip-components=1 \  
&& rm ts.tar.bz2 \  
&& cd /opt/src/ts \  
&& ./configure --prefix=/opt/ts \  
&& make \  
&& make install \  
&& rm -r /opt/src/ts  
  
COPY start.sh /start.sh  
  
ENV TS_PORT 8080  
ENV TS_STORAGE_SIZE 256M  
  
ENV PROXY_CONFIG_HTTP_SERVER_PORTS $TS_PORT  
  
EXPOSE $TS_PORT  
  
CMD ["/start.sh"]  

