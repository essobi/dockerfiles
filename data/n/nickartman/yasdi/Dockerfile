FROM debian:latest  
MAINTAINER Nick Artman<nick@addosolutions.com>  
  
  
WORKDIR /usr/src  
  
RUN apt-get update; \  
apt-get -y install wget make cmake unzip;\  
wget http://files.sma.de/dl/11705/yasdi-1.8.1build9-src.zip; \  
unzip yasdi-1.8.1build9-src.zip; \  
mkdir /usr/src/projects/generic-cmake/build-gcc  
  
WORKDIR /usr/src/projects/generic-cmake/build-gcc  
  
RUN cmake ..; \  
make; \  
make install; \  
apt-get clean; \  
rm -rf /usr/src/*;  
  
WORKDIR /  
  
ENV LD_LIBRARY_PATH /usr/local/lib  

