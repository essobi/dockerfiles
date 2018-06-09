FROM debian:jessie  
  
# install needed libraries  
  
RUN deps='ca-certificates libbz2-1.0 libgdbm3 libreadline6 libsqlite3-0
libssl1.0.0 xz-utils zlib1g'; \  
set -x \  
&& apt-get update \  
&& apt-get install -y $deps --no-install-recommends  
  
# install stackless in /opt/stackless  
  
RUN BUILD_DEPS='bzip2 curl gcc libbz2-dev libgdbm-dev libc6-dev
libreadline6-dev libsqlite3-dev libssl-dev make zlib1g-dev'; \  
set -x \  
&& apt-get update \  
&& apt-get install -y $BUILD_DEPS --no-install-recommends \  
&& mkdir -p /usr/src/python \  
&& curl -s http://www.stackless.com/binaries/stackless-2714-export.tar.xz |
tar -xJC /usr/src/python --strip-components=1 \  
&& cd /usr/src/python \  
&& ./configure --prefix=/opt/stackless \  
&& make -j$(nproc) \  
&& make install \  
&& cd / \  
&& rm -rf /usr/src/python \  
&& /opt/stackless/bin/python -m ensurepip \  
&& /opt/stackless/bin/pip install --upgrade pip setuptools virtualenv \  
&& apt-get purge -y --auto-remove $BUILD_DEPS  

