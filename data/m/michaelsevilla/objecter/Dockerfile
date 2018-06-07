FROM ubuntu:trusty  
  
MAINTAINER Michael Sevilla <mikesevilla3@gmail.com>  
  
ARG DEBIAN_FRONTEND=noninteractive  
RUN apt-get update -y && \  
apt-get install -y cmake3 g++ liblua5.1-0-dev libboost-serialization-dev && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /root  
ADD entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  

