FROM ubuntu:14.04  
MAINTAINER Sylvain Deloux <docker@eax.fr>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y automake git make && \  
apt-get install -y libcurl4-openssl-dev  
  
RUN git clone https://github.com/pooler/cpuminer && \  
cd cpuminer && \  
./autogen.sh && \  
./configure CFLAGS="-O3" && \  
make  
  
WORKDIR /cpuminer  
  
ENTRYPOINT ["./minerd"]  

