FROM ubuntu:latest  
MAINTAINER Rafal Sladek <rafal.sladek@gmail>  
  
WORKDIR /root  
  
ENV RED '\033[0;31m'  
ENV GREEN '\033[0;32m'  
ENV NC '\033[0m'  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM dumb  
  
RUN apt-get update >/dev/null 2>&1  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y -qq upgrade  
  
RUN apt install -y software-properties-common  
  
RUN apt-add-repository -y ppa:bitcoin/bitcoin  
  
RUN apt-get update >/dev/null 2>&1  
  
RUN apt install -y \  
make software-properties-common \  
build-essential libtool autoconf \  
libssl-dev libboost-dev \  
libboost-chrono-dev \  
libboost-filesystem-dev \  
libboost-program-options-dev \  
libboost-system-dev libboost-test-dev \  
libboost-thread-dev sudo automake \  
git wget pwgen curl libdb4.8-dev \  
bsdmainutils libdb4.8++-dev \  
libminiupnpc-dev libgmp3-dev \  
ufw fail2ban pwgen

