FROM debian:jessie  
MAINTAINER Sergey Besedin "kr3ssh@gmail.com"  
RUN echo 'deb-src http://http.debian.net/debian jessie main' >>
/etc/apt/sources.list  
  
ENV DEBIAN_FRONTEND noninteractive  
  
#Setup build environment for libpam  
RUN apt-get update && apt-get -y build-dep pam  
  
#Rebuild and istall libpam with --disable-audit option  
RUN export CONFIGURE_OPTS=--disable-audit && cd /root && apt-get -b source pam
&& dpkg -i libpam-doc*.deb libpam-modules*.deb libpam-runtime*.deb
libpam0g*.deb  
  
RUN apt-get clean  
  
RUN rm -rf /root/pam* /root/libpam*  

