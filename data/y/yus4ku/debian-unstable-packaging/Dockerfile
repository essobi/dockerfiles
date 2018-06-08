FROM debian:unstable  
MAINTAINER Yusaku OGAWA <yus4ku@gmail.com>  
  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y packaging-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  

