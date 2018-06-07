FROM phusion/baseimage:0.9.22  
MAINTAINER Zhan.Shi <g.shizhan.g@gmail.com>  
  
RUN apt-get update && apt-get install -y wget \  
build-essential \  
cmake \  
libboost-math-dev \  
libboost-program-options-dev \  
libboost-test-dev \  
libboost-serialization-dev \  
libarmadillo-dev \  
binutils-dev  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
RUN wget http://www.mlpack.org/files/mlpack-2.1.1.tar.gz && tar xzf
mlpack-2.1.1.tar.gz && rm mlpack-2.1.1.tar.gz  
RUN cd mlpack-2.1.1 && mkdir build && cd build && cmake -D DEBUG=OFF -D
PROFILE=OFF ../ && make && make install && make clean  
  
VOLUME /datasets  
WORKDIR /datasets  
  
ENV LD_LIBRARY_PATH /usr/local/lib  
  
CMD ["/sbin/init"]  

