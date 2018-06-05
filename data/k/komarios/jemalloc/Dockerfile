FROM ubuntu:latest  
LABEL maintainer="Kogias Marios"  
  
ENV DEBIAN_FRONTEND=noninteractive \  
JEMALLOC_VERSION=5.0.1  
  
RUN apt-get update && \  
apt-get install -yq wget pwgen gcc make bzip2 && \  
rm -rf /var/lib/apt/lists/* && \  
wget -q
https://github.com/jemalloc/jemalloc/releases/download/$JEMALLOC_VERSION/jemalloc-$JEMALLOC_VERSION.tar.bz2
&& \  
tar jxf jemalloc-*.tar.bz2 && \  
rm jemalloc-*.tar.bz2 && \  
cd jemalloc-* && \  
./configure --enable-prof --enable-stats --enable-debug --enable-fill && \  
make && \  
make install && \  
cd - && \  
rm -rf jemalloc-* && \  
apt-get remove -yq wget pwgen gcc make bzip2 && \  
rm -rf /usr/share/doc /usr/share/man && \  
apt-get clean autoclean && \  
apt-get autoremove -y && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
ENV LD_PRELOAD=/usr/local/lib/libjemalloc.so \  
MALLOC_CONF=prof:true,prof_leak:true,lg_prof_interval:26,lg_prof_sample:16  

