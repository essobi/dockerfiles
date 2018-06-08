#  
# Dockerfile to build a new syndicate (SYNX) release  
# https://bitcointalk.org/index.php?topic=1511215.0  
# _____ _ _ _  
# | __|_ _ ___ _| |_|___ ___| |_ ___  
# |__ | | | | . | | _| .'| _| -_|  
# |_____|_ |_|_|___|_|___|__,|_| |___|  
# |___|  
#  
# tip me at:  
# BTC 1PboFDkBsW2i968UnehWwcSrM9Djq5LcLB  
# SYNX SSKYwMhQQt9DcWozt7zA1tR3DmRuw1gT6b  
#  
# usage: docker run marsmensch/synx:latest  
#  
# BUILD DOCKER: docker build -t marsmensch/synx:latest .  
# RUN DOCKER: docker run -it marsmensch/synx  
# TEST DOCKER: docker run --interactive --tty --entrypoint=/bin/bash
marsmensch/synx  
#  
FROM ubuntu:16.04  
MAINTAINER Florian Maier <contact@marsmenschen.com>  
ENV REFRESHED_AT 2016-07-11  
# Set environment variables (can be changed on docker run with -e)  
ENV GIT_PROJECT SyndicateQT  
ENV PROJ_GIT_URL git://github.com/marsmensch/${GIT_PROJECT}.git  
ENV SYNX_CONF /root/.Syndicate/Syndicate.conf  
#ENV SYNX_VERSION v1.0.0.6.1  
ENV SYNX_VERSION master  
  
# install dependencies  
RUN export DEBIAN_FRONTEND=noninteractive && apt-get autoclean && apt-get
autoremove && apt-get update && \  
apt-get -qqy install --no-install-recommends build-essential automake
libleveldb-dev \  
libcurl4-openssl-dev libssl-dev make autoconf automake libtool git apt-utils
libgmp-dev \  
libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools
libprotobuf-dev protobuf-compiler \  
libboost-dev libboost-system-dev libboost-filesystem-dev libboost-program-
options-dev pkg-config \  
libdb++-dev libminiupnpc-dev libqt5webkit5-dev libcurl3-dev libudev-dev
libboost-all-dev && \  
rm -rf /var/lib/apt/lists/*  
  
# build steps for linux  
# 1) clone the Syndicate code directory  
# 2) build Syndicated without upnp support (recommended)  
# 3) build the qt wallet  
RUN mkdir -p /opt/code/; cd /opt/code; git clone ${PROJ_GIT_URL}
${GIT_PROJECT} && \  
cd /opt/code/${GIT_PROJECT}/src && git checkout ${SYNX_VERSION} && make -f
makefile.unix USE_UPNP= && \  
chmod u+x /opt/code/${GIT_PROJECT}/src/leveldb/build_detect_platform && \  
chmod u+x /opt/code/${GIT_PROJECT}/src/secp256k1/autogen.sh && cd .. && \  
qmake -qt=qt5 USE_UPNP= && make && cp Syndicate-qt src/Syndicated
/usr/local/bin/ && \  
rm -rf /opt/code/  
  
# generate a dummy config  
RUN PASS=$(date | md5sum | cut -c1-24); mkdir -p /root/.Syndicate/; \  
printf '%s\n%s\n%s\n%s\n%s\n' "rpcuser=syndicaterpc" "rpcpassword=${PASS}" \  
"addnode=107.170.206.191" "addnode=192.241.237.60" "addnode=192.241.215.173" \  
"addnode=162.243.130.27" "addnode=162.243.131.87" "addnode=104.131.145.170" \  
"addnode=104.131.58.180" "addnode=104.236.233.90" "addnode=45.55.179.6" \  
"addnode=45.55.181.27" "addnode=45.55.181.37" "addnode=198.199.100.4" \  
"server=1" "listen=1" "daemon=1" "logtimestamps=1" "mnconflock=0" >>
${SYNX_CONF}

