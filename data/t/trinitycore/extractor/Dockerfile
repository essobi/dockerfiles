# This container generates the DBC, maps, vmaps, and mmaps  
# Maintainer: Will Blankenship <william.jblankenship@gmail.com>  
FROM debian:jessie  
  
RUN apt-get update && \  
apt-get install --force-yes -y \  
autoconf \  
build-essential \  
cmake \  
gcc \  
g++ \  
git \  
libtool \  
make \  
libncurses5-dev \  
openssl \  
libssl-dev \  
libmysqlclient15-dev \  
libmysql++-dev \  
libreadline6-dev \  
zlib1g-dev \  
libbz2-dev \  
libboost-dev \  
libboost-thread-dev \  
libboost-system-dev \  
libboost-filesystem-dev \  
libboost-program-options-dev \  
libzmq-dev  
  
RUN mkdir tools  
  
ADD mapextractor /tools/mapextractor  
ADD vmap4extractor /tools/vmap4extractor  
ADD vmap4assembler /tools/vmap4assembler  
ADD mmaps_generator /tools/mmaps_generator  
ADD script.sh script.sh  
RUN chmod +x script.sh && chmod +x /tools/*  
  
CMD ["./script.sh"]  

