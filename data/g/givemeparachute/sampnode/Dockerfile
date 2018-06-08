# Dockerfile for SAMP on Pterodactyl Panel  
# && apt-add-architecture i386 \  
FROM frolvlad/alpine-glibc  
#FROM ubuntu:16.04  
#FROM centos:latest  
  
MAINTAINER Stefano Ortiz <staff+staff@comugamers.com>  
  
RUN apk update \  
&& apk upgrade \  
&& echo "http://nl.alpinelinux.org/alpine/latest-stable/main/" >>
/etc/apk/repositories \  
&& apk add \--no-cache curl bash ca-certificates openssl perl wget psmisc
libstdc++ \  
&& apk update \  
&& apk upgrade \  
&& adduser -D -h /home/container container  
  
USER container  
ENV USER container  
ENV HOME /home/container  
  
WORKDIR /home/container  
  
COPY ./start.sh /start.sh  
  
CMD ["/bin/bash", "/start.sh"]  

