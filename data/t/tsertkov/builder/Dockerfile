# Docker-Builder  
#  
# VERSION 0.1  
FROM ubuntu:latest  
MAINTAINER tsertkov <tsertkov@gmail.com>  
  
ENV TERM linux  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install \  
build-essential \  
golang \  
git \  
mercurial  
  
VOLUME ["/build", "/src"]  
WORKDIR /src  
CMD ["/build/build.sh"]  
ENTRYPOINT ["/bin/sh"]  

