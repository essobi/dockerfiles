FROM phusion/baseimage:latest  
  
MAINTAINER G De Gasperis <giovanni@giodegas.it>  
  
RUN apt-get update && apt-get upgrade -q -y && \  
apt-get install -q -y build-essential autogen autoconf automake git
libcurl4-openssl-dev libgmp-dev libjansson-dev  
RUN git clone https://github.com/magi-project/m-cpuminer-v2.git && cd
m-cpuminer-v2  
WORKDIR /m-cpuminer-v2  
RUN ./autogen.sh && ./configure CFLAGS="-O3" CXXFLAGS="-O3" && make  
  

