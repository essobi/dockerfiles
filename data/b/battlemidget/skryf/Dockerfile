#  
# Skryf  
#  
# https://github.com/skryf/Skryf  
FROM ubuntu:13.10  
MAINTAINER Adam Stokes <adamjs@cpan.org>  
  
# locales  
ENV DEBIAN_FRONTEND noninteractive  
RUN locale-gen en_US.UTF-8 && dpkg-reconfigure locales  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu saucy main universe multiverse"
> /etc/apt/sources.list  
RUN echo "deb http://archive.ubuntu.com/ubuntu saucy-updates main universe
multiverse" >> /etc/apt/sources.list  
RUN echo "deb http://archive.ubuntu.com/ubuntu saucy-proposed main universe
multiverse" >> /etc/apt/sources.list  
  
RUN apt-get update  
RUN apt-get upgrade -y  
  
# Install basic packages.  
RUN apt-get install -y curl git perl perl-modules cpanminus cpanoutdated
build-essential mongodb-server mongodb-clients  
RUN service mongodb start  
  
ENV HOME /root  
WORKDIR /root  
  
RUN cpanm --notest https://github.com/skryf/Skryf/archive/v1.0.7.tar.gz  

