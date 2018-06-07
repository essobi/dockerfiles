FROM ubuntu:xenial  
MAINTAINER Pheoxy  
  
  
# global environment settings  
ENV DEBIAN_FRONTEND="noninteractive"  
VOLUME /config  
#WORKDIR /config  
# install packages  
RUN apt-get update && apt-get install -y \  
build-essential \  
file \  
g++ \  
gawk \  
gettext \  
git \  
libncurses5-dev \  
libssl-dev \  
python \  
rsync \  
subversion \  
unzip \  
wget \  
zlib1g-dev && \  
# lede source  
#git clone https://git.lede-project.org/source.git lede && \  
# cd lede && \  
# ./scripts/feeds update -a && \  
# ./scripts/feeds install -a && \  
# make defconfig && \  
# cleanup  
apt-get clean && \  
rm -rf \  
/tmp/* \  
/var/lib/apt/lists/* \  
/var/tmp/*  

