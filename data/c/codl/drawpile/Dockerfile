FROM ubuntu:xenial  
MAINTAINER Corentin Delcourt <codl@codl.fr>  
  
ENV DRAWPILE_VERSION 2.0.10  
RUN apt-get update && \  
apt-get install -y cmake extra-cmake-modules qtbase5-dev g++ curl
libkf5archive-dev && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /tmp  
  
RUN curl -s https://drawpile.net/files/src/drawpile-${DRAWPILE_VERSION}.tar.gz
\  
| gunzip | tar -x  
  
RUN mkdir -p /tmp/drawpile-build && \  
cd /tmp/drawpile-build && \  
cmake /tmp/drawpile-${DRAWPILE_VERSION} -DCMAKE_INSTALL_PREFIX=/usr
-DCLIENT=off -DSERVERGUI=OFF && \  
make install && \  
useradd --system drawpile && \  
cd / && rm -rf /tmp/drawpile-${DRAWPILE_VERSION} /tmp/drawpile-build  
  
WORKDIR /  
  
ENTRYPOINT ["/usr/bin/drawpile-srv"]  
  
USER drawpile  
EXPOSE 27750  

