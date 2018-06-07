FROM phusion/baseimage:0.9.19  
MAINTAINER educatedwarrior  
  
# Configuration variables  
#test or prod for NODE_TYPE  
ENV TERM=xterm  
ENV LANG=en_US.UTF-8  
  
RUN \  
apt-get update && \  
apt-get install -y \  
autoconf \  
automake \  
autotools-dev \  
build-essential \  
cmake \  
doxygen \  
libboost-all-dev \  
libreadline-dev \  
libssl-dev \  
libtool \  
ncurses-dev \  
gcc-4.9 g++-4.9 \  
libbz2-dev libdb++-dev libdb-dev \  
python3 \  
python3-dev \  
python3-jinja2 \  
python3-pip \  
wget \  
screen \  
git && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
  
#Install required version of boost  
RUN \  
cd /tmp && wget
https://cytranet.dl.sourceforge.net/project/boost/boost/1.59.0/boost_1_59_0.tar.bz2
&& \  
tar xvf boost_1_59_0.tar.bz2 && \  
cd boost_1_59_0 && \  
./bootstrap.sh --prefix=/usr/local --with-libraries=all
--libdir=/usr/local/lib --includedir=/usr/local/include && \  
./b2 install && \  
rm -rf /tmp/boost_1_59_0*  
  
CMD /bin/sh

