FROM ubuntu:17.04  
MAINTAINER RazzDazz  
  
ENV REFRESHED_AT 2017-06-29  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update packages to install java  
RUN apt-get -yqq update && \  
apt-get -yqq upgrade && \  
apt-get \--no-install-recommends -yqq install openjdk-8-jre-headless && \  
rm -rf /var/lib/apt/lists/*  

