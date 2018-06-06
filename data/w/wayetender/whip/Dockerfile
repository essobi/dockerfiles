FROM python:2.7  
MAINTAINER Lucas Waye <lucas@lucaswaye.com>  
  
WORKDIR /whip  
COPY src src  
ENV THRIFT_VERSION 0.9.3  
RUN buildDeps=" \  
automake \  
bison \  
curl \  
flex \  
g++ \  
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
&& curl -sSL
"http://apache.mirrors.spacedump.net/thrift/$THRIFT_VERSION/thrift-$THRIFT_VERSION.tar.gz"
-o thrift.tar.gz \  
&& mkdir -p /usr/src/thrift \  
&& tar zxf thrift.tar.gz -C /usr/src/thrift --strip-components=1 \  
&& rm thrift.tar.gz \  
&& cd /usr/src/thrift \  
&& ./configure --without-tests --without-python --with-cpp \  
&& make \  
&& make install \  
&& cd / \  
&& rm -rf /usr/src/thrift \  
&& pip install -r /whip/src/adapter/requirements.txt \  
&& /whip/src/adapter/update-stubs.sh \  
&& /whip/src/adapter/regen-parser.sh \  
&& cd /whip/src/shim/linux \  
&& make \  
&& apt-get purge -y --auto-remove $buildDeps  
  
ENV PATH "$PATH:/whip/src/bin"  

