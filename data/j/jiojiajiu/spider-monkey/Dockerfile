FROM ubuntu:latest  
MAINTAINER Bokum Guro <jiojiajiu@gmail.com>  
  
RUN apt-get update && \  
apt-get -y install build-essential wget python2.7 python2.7-dev && \  
apt-get -y clean  
  
ENV SHELL /bin/bash  
RUN wget https://people.mozilla.org/~sstangl/mozjs-31.5.0.tar.bz2 -O
/usr/src/mozjs-31.5.0.tar.bz2 && \  
cd /usr/src/ && tar xvf mozjs-31.5.0.tar.bz2 && rm mozjs-31.5.0.tar.bz2 && \  
cd mozjs-31.5.0/js/src && ./configure && make -j1 && make install && make
clean  

