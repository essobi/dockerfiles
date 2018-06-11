FROM lsiobase/xenial  
MAINTAINER Mike Weaver <>  
  
# set version label  
ARG BUILD_DATE  
ARG VERSION  
LABEL build_version="Linuxserver.io version:- ${VERSION} Build-date:-
${BUILD_DATE}"  
  
# global environment settings  
ENV DEBIAN_FRONTEND="noninteractive" \  
SOURCE_URL="https://hndl.urbackup.org/Server/2.2.11/urbackup-
server-2.2.11.tar.gz"  
RUN \  
apt-get update && \  
apt-get install -y debconf sqlite3 libc6 libcrypto++9v5 libcurl3 libfuse2
libgcc1 libstdc++6 zlib1g debconf libguestfs-tools qemu-utils make gcc g++
zlib1g-dev libcurl4-openssl-dev libcrypto++-dev libfuse-dev pkg-config  
  
RUN curl ${SOURCE_URL} | \  
tar -xzC /tmp/ && \  
cd /tmp/urbackup* && \  
sed -i -e 's/C\:\\\\\\\urbackup/\/config\//g'
urbackupserver/server_settings.cpp && \  
./configure --with-mountvhd && \  
make && \  
make install  
  
# cleanup  
RUN apt-get autoremove -y make gcc g++ zlib1g-dev libcurl4-openssl-dev
libcrypto++-dev libfuse-dev pkg-config && \  
apt-get clean && \  
rm -rf \  
/tmp/* \  
/var/lib/apt/lists/* \  
/var/tmp/*  
  
COPY root/ /  
  
EXPOSE 55413 55414 55415 35623/udp  
  
VOLUME /var/urbackup /var/log /usr/share/urbackup  

