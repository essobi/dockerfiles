FROM ubuntu:precise  
MAINTAINER Lex Lapax <lexlapax@gmail.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo "deb http://us.archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
RUN \  
apt-get update ;\  
apt-get upgrade -y ;\  
apt-get install build-essential libtool libssl-dev python-distutils-extra
python-software-properties wget curl git -y  
  
CMD ["/bin/bash", "-i"]  

