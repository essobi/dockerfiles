# ubuntu 14.04 (Trusty Tahr)  
FROM ubuntu  
  
RUN echo "deb http://jp.archive.ubuntu.com/ubuntu/ trusty main restricted\n \  
deb-src http://jp.archive.ubuntu.com/ubuntu/ trusty main restricted\n \  
deb http://jp.archive.ubuntu.com/ubuntu/ trusty-updates main restricted\n \  
deb-src http://jp.archive.ubuntu.com/ubuntu/ trusty-updates main restricted\n
\  
deb http://jp.archive.ubuntu.com/ubuntu/ trusty universe\n \  
deb-src http://jp.archive.ubuntu.com/ubuntu/ trusty universe\n \  
deb http://jp.archive.ubuntu.com/ubuntu/ trusty-updates universe\n \  
deb-src http://jp.archive.ubuntu.com/ubuntu/ trusty-updates universe\n \  
deb http://jp.archive.ubuntu.com/ubuntu/ trusty multiverse\n \  
deb-src http://jp.archive.ubuntu.com/ubuntu/ trusty multiverse\n \  
deb http://jp.archive.ubuntu.com/ubuntu/ trusty-updates multiverse\n \  
deb-src http://jp.archive.ubuntu.com/ubuntu/ trusty-updates multiverse\n \  
deb http://jp.archive.ubuntu.com/ubuntu/ trusty-backports main restricted
universe multiverse\n \  
deb-src http://jp.archive.ubuntu.com/ubuntu/ trusty-backports main restricted
universe multiverse\n \  
deb http://security.ubuntu.com/ubuntu trusty-security main restricted\n \  
deb-src http://security.ubuntu.com/ubuntu trusty-security main restricted\n \  
deb http://security.ubuntu.com/ubuntu trusty-security universe\n \  
deb-src http://security.ubuntu.com/ubuntu trusty-security universe\n \  
deb http://security.ubuntu.com/ubuntu trusty-security multiverse\n \  
deb-src http://security.ubuntu.com/ubuntu trusty-security multiverse\n" \  
> /etc/apt/sources.list  
  
RUN apt-get update  
  
RUN apt-get install -y \  
git \  
gcc \  
autoconf \  
automake \  
pkg-config \  
make \  
libtool \  
libpcre3-dev \  
libcap-dev \  
libncurses5-dev \  
openssl \  
tcl-dev \  
expat \  
flex \  
hwloc \  
curl \  
zlib1g-dev \  
libcunit1-dev \  
libevent-dev \  
libssl-dev \  
libxml2-dev \  
libjansson-dev \  
libjemalloc-dev  
  
WORKDIR /opt  
  
RUN ldconfig  
  
RUN git clone --depth 1 https://github.com/openssl/openssl.git  
RUN cd openssl && \  
./config shared zlib && \  
make && \  
make install  
  
RUN git clone --depth 1 https://github.com/tatsuhiro-t/spdylay.git  
RUN cd spdylay && \  
autoreconf -i && \  
automake && \  
autoconf && \  
./configure && \  
make && \  
make install  
  
RUN git clone --depth 1 https://github.com/tatsuhiro-t/nghttp2.git  
RUN cd nghttp2 && \  
autoreconf -i && \  
automake && \  
autoconf && \  
./configure --enable-app && \  
make && \  
make install  
  
RUN git clone --depth 1 https://github.com/apache/trafficserver.git  
RUN cd trafficserver && \  
git submodule update --depth 1 && \  
autoreconf -if && \  
./configure --enable-spdy && \  
make && \  
make check && \  
make install  
  
RUN ldconfig  
CMD service rsyslog start  

