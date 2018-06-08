FROM debian:wheezy  
MAINTAINER Adam Hawkins <adam@saltside.se>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV THRIFT_VERSION 0.9.2  
  
RUN buildDeps=" \  
autoconf \  
bison \  
curl \  
flex \  
g++ \  
git \  
libboost-dev \  
libboost-filesystem-dev \  
libboost-program-options-dev \  
libboost-system-dev \  
libboost-test-dev \  
libevent-dev \  
libssl-dev \  
libtool \  
make \  
pkg-config \  
"; \  
apt-get update && apt-get install -y --no-install-recommends $buildDeps && rm
-rf /var/lib/apt/lists/* \  
&& curl -k -sSL "https://storage.googleapis.com/golang/go1.3.3.linux-
amd64.tar.gz" -o go.tar.gz \  
&& tar xzf go.tar.gz \  
&& rm go.tar.gz \  
&& cp go/bin/gofmt /usr/bin/gofmt \  
&& rm -rf go \  
&& curl -k -sSL
"http://ftp.debian.org/debian/pool/main/a/automake-1.14/automake_1.14.1-4_all.deb"
-o automake_1.14.1-4_all.deb \  
&& dpkg -i automake_1.14.1-4_all.deb \  
&& rm automake_1.14.1-4_all.deb \  
&& git clone git://github.com/Saltside/thrift /usr/src/thrift \  
&& cd /usr/src/thrift \  
&& ./bootstrap.sh \  
&& ./configure --without-python --without-cpp \  
&& make \  
&& make install \  
&& cd / \  
&& rm -rf /usr/src/thrift \  
&& apt-get purge -y --auto-remove $buildDeps  
  
ENTRYPOINT ["thrift"]  

