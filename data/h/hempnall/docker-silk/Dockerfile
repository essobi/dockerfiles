FROM ubuntu:14.04  
RUN apt-get update && apt-get -y install man build-essential pkg-config
libglib2.0-dev  
ADD libfixbuf-1.6.1.tar.gz /build  
ADD silk-3.9.0.tar.gz /build  
WORKDIR /build/libfixbuf-1.6.1  
RUN ./configure && make && make install  
WORKDIR /build/silk-3.9.0  
RUN ./configure && make && make install  

