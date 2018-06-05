# https://github.com/tgraf/bmon/  
FROM ubuntu:latest  
MAINTAINER sthysel <sthysel@gmail.com>  
ENV REFRESHED_AT 2016-01-19  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
apt-transport-https \  
build-essential \  
git \  
autoconf \  
automake \  
make \  
libconfuse-dev \  
libnl-3-dev \  
libnl-route-3-dev \  
libncurses-dev \  
pkg-config  
  
WORKDIR /src/  
RUN git clone https://github.com/tgraf/bmon.git  
RUN cd bmon && ./autogen.sh && ./configure && make && make install  
  
CMD ["bmon"]  

