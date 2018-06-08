#  
# Dockerfile to build a new Gambit release  
#  
# BUILD: docker build -t marsmensch/gambitcrypto:latest .  
# RUN: docker run -it marsmensch/gambitcrypto  
# TEST: docker run --interactive --tty --entrypoint=/bin/bash
marsmensch/gambitcrypto  
#  
FROM ubuntu:16.04  
MAINTAINER Florian Maier <contact@marsmenschen.com>  
ENV REFRESHED_AT 2016-05-16  
# Set environment variables (can be changed on docker run with -e)  
ENV GIT_PROJECT gambitcrypto  
ENV CODE_DIR /opt/code/${GIT_PROJECT}  
ENV GAM_GIT_URL git://github.com/marsmensch/${GIT_PROJECT}.git  
  
# install dependencies  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
apt-get -qqy install --no-install-recommends build-essential automake
libleveldb-dev \  
libcurl4-openssl-dev libssl-dev make autoconf automake libtool git apt-utils \  
pkg-config qt4-qmake libqt4-dev libboost-all-dev libboost-dev libboost-system-
dev \  
libboost-filesystem-dev libboost-program-options-dev libdb++-dev libminiupnpc-
dev \  
libcurl3-dev libudev-dev && apt-get autoclean && apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
# Gambit code directory  
RUN mkdir -p /opt/code/; cd /opt/code; git clone ${GAM_GIT_URL} ${GIT_PROJECT}
&& \  
cd ${CODE_DIR} && qmake RELEASE=1 USE_UPNP=1 USE_O3=1 && make && \  
cd src && make -f makefile.unix USE_UPNP=1 STATIC=1 USE_O3=1 && \  
cd ${CODE_DIR} && cp gambit-qt src/gambitd /usr/local/bin/ && \  
rm -rf /opt/code/

