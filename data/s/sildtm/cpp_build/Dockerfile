FROM alpine:latest  
MAINTAINER Dilletante <thedilletante@gmail.com>  
  
RUN \  
apk add \--update openssl && \  
apk add make gcc g++ cmake openssl-dev linux-headers git && \  
cd /tmp/ && \  
wget
https://sourceforge.net/projects/boost/files/boost/1.63.0/boost_1_63_0.zip/download
-O boost_1_63_0.zip && \  
unzip boost_1_63_0.zip && \  
cd boost_1_63_0/ && \  
./bootstrap.sh && ./b2 install && \  
cd .. && rm -rf boost_1_63_0*  

