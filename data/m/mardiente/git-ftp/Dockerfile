FROM debian:stable-slim  
MAINTAINER Mark Ardiente <mark.ardiente@acidgreen.com.au>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# setup workdir  
RUN mkdir -p /root/work/  
WORKDIR /root/work/  
  
ARG CACHE_DATE=2018-08-30  
# install git  
RUN apt-get -y update && apt-get -y install git && apt-get -y install git-ftp  
  
ARG GIT_FTP_VERSION=master  
# replace with latest version  
RUN curl https://raw.githubusercontent.com/git-ftp/git-
ftp/${GIT_FTP_VERSION}/git-ftp > /usr/bin/git-ftp  
  
# slim down image  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/usr/share/man/?? /usr/share/man/??_*  
  

