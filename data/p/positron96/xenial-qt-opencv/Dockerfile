# Minimal docker container to build project  
FROM ubuntu:xenial  
MAINTAINER positron96  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install updates & requirements:  
RUN apt-get -qq update && apt-get -qq dist-upgrade && apt-get install -qq -y
--no-install-recommends \  
git \  
openssh-client \  
ca-certificates \  
build-essential \  
pkg-config \  
&& apt-get -qq clean  
  
RUN apt-get install -y qtbase5-dev qt5-default && apt-get -qq clean  
  
RUN apt-get install -y libopencv-dev && apt-get -qq clean  
  
RUN echo 'root:root' | chpasswd  
  
WORKDIR /root  
  

