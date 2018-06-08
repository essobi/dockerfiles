FROM ubuntu:16.04  
  
MAINTAINER fractalyse <fractalyse@users.noreply.github.com>  
LABEL description="Ubuntu 16.04 with pre-installed dependency for masternode"  
  
WORKDIR /tmp  
  
RUN apt-get update \  
&& apt-get install -y python-software-properties \  
&& apt-get install -y software-properties-common \  
&& add-apt-repository ppa:bitcoin/bitcoin \  
&& apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y pkg-config build-essential autoconf automake libtool
libboost-all-dev libgmp-dev libssl-dev libcurl4-openssl-dev libdb4.8-dev
libdb4.8++-dev libevent-dev wget git nano \  
&& apt-get -y autoremove \  
&& apt-get clean autoclean \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}  
  
CMD ["/bin/bash"]

