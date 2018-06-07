FROM debian:jessie  
MAINTAINER Jihoon Chung <jihoon@gmail.com>  
  
# setup build env  
RUN apt-get update && \  
apt-get -y install pkg-config wget make binutils autoconf automake autotools-
dev libtool libssl-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# build nghttp2-lib  
ENV NGHTTP2_VERSION=1.1.2  
RUN cd /usr/local/src && \  
wget -q -O-
https://github.com/tatsuhiro-t/nghttp2/releases/download/v${NGHTTP2_VERSION}/nghttp2-${NGHTTP2_VERSION}.tar.gz
| tar xzf - && \  
cd /usr/local/src/nghttp2-${NGHTTP2_VERSION} && \  
./configure --prefix=/usr --disable-app --disable-hpack-tools --disable-asio-
lib --disable-examples --disable-python-bindings && \  
make && \  
make install && \  
rm -rf /usr/local/src/nghttp2-${NGHTTP2_VERSION}  
  
# build curl  
ENV CURL_VERSION=7.44.0  
RUN cd /usr/local/src && \  
wget -q -O- http://curl.haxx.se/download/curl-${CURL_VERSION}.tar.gz | tar xzf
- && \  
cd /usr/local/src/curl-${CURL_VERSION} && \  
./configure --prefix=/usr/local \--enable-http --with-nghttp2 && \  
make && \  
make install && \  
rm -rf /usr/local/src/curl-${CURL_VERSION}  
  
ENV LD_LIBRARY_PATH=/usr/local/lib  
  
ENTRYPOINT ["/usr/local/bin/curl"]  
  
CMD ["--help"]  

