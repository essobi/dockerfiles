FROM ubuntu:14.04  
MAINTAINER Zhuyi Xue <alfred532008@gmail.com>  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && apt-get -y install \  
autoconf \  
build-essential \  
libboost-all-dev \  
libcurl4-openssl-dev \  
libssl-dev \  
libtool \  
libxerces-c-dev \  
libxqilla-dev \  
python \  
wget  
  
# touch .git is a strange step probably due to bug in the code, learned from  
# Kevin's blog  
# http://iokevins.blogspot.ca/2015/02/genetorrent-building-release-387-on.html  
RUN wget https://bitbucket.org/cghub/genetorrent/get/3.8.6.tar.gz \  
&& tar zxf 3.8.6.tar.gz \  
&& cd cghub-genetorrent-097c9fdff2ff \  
&& touch .git \  
&& ./autogen.sh \  
&& ./configure \  
&& make \  
&& make install \  
&& cd .. && rm -rf 3.8.6.tar.gz cghub-genetorrent-097c9fdff2ff  
  
# otherwise gtdownload cannot find libgenetorrent.so.00  
ENV LD_LIBRARY_PATH=/usr/local/lib/  
  
CMD ["cgquery", "--help"]  

