FROM debian  
  
MAINTAINER Chad Lyon "http://github.com/chadlyon"  
# Update the package repository  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get upgrade -y && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y wget curl git locales build-
essential pkg-config dh-autoreconf bzip2 \  
libpcre3-dev tcl-dev libboost-dev zlib1g-dev libcunit1-dev libssl-dev
libxml2-dev libev-dev libevent-dev libjansson-dev \  
libjemalloc-dev cython python3.4-dev python-setuptools gawk  
  
# Configure locale  
RUN export LANGUAGE=en_US.UTF-8 && \  
export LANG=en_US.UTF-8 && \  
export LC_ALL=en_US.UTF-8 && \  
locale-gen en_US.UTF-8 && \  
DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales  
  
# Install SPDY  
RUN git clone https://github.com/tatsuhiro-t/spdylay /downloads/spdylay  
RUN cd /downloads/spdylay/ && autoreconf -if && ./configure
--prefix=/opt/spdylay && make install  
  
# Install nghttp2  
RUN git clone \--depth 1 https://github.com/tatsuhiro-t/nghttp2.git
/downloads/nghttp2  
RUN cd /downloads/nghttp2 && autoreconf -i && automake && autoconf &&
PKG_CONFIG_PATH=/opt/spdylay/lib/pkgconfig/ ./configure --enable-app && make
&& make install  
  
# Install TrafficServer  
RUN mkdir -p /downloads/trafficserver  
RUN wget
http://download.nextag.com/apache/trafficserver/trafficserver-5.3.1.tar.bz2 -O
/downloads/trafficserver.tar.bz2  
RUN cd /downloads && tar xvf trafficserver.tar.bz2 -C /downloads/trafficserver
--strip-components 1  
RUN cd /downloads/trafficserver && PKG_CONFIG_PATH=/opt/spdylay/lib/pkgconfig/
./configure --prefix=/opt/trafficserver --enable-spdy  
RUN cd /downloads/trafficserver && make  
RUN cd /downloads/trafficserver && make install  
#RUN rm -rf /opt/trafficserver/etc/trafficserver  
#ADD ./files/etc/trafficserver /etc/trafficserver  
RUN mv /opt/trafficserver/etc/trafficserver /etc/trafficserver  
RUN ln -sf /etc/trafficserver /opt/trafficserver/etc/trafficserver  
  
# tail the logs so they appear in STDOUT  
RUN tail -F /opt/trafficserver/var/log/trafficserver/diags.log &  
RUN tail -F /opt/trafficserver/var/log/trafficserver/squid.log &  
  
EXPOSE 8080  
CMD ["/opt/trafficserver/bin/traffic_cop"]  

