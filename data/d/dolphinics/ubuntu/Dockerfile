FROM ubuntu:14.04  
MAINTAINER Dolphinics  
RUN apt-get update && apt-get -y install autoconf make libtool gcc g++
libqt4-dev pkg-config linux-headers-generic build-essential git  
  
#install fake uname  
COPY uname.sh /  
RUN /uname.sh --install $(ls /lib/modules/ | head -n 1)  

