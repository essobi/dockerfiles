FROM ubuntu:latest  
  
MAINTAINER basherone <basherone123@gmail.com>  
  
RUN echo "deb http://shadowsocks.org/ubuntu trusty main" >>
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get install -y --force-yes shadowsocks-libev libssl-dev  
  
ENTRYPOINT ["/usr/bin/ss-server"]  
  

