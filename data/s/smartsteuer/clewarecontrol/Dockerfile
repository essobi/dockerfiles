# Use phusion/baseimage as base image. To make your builds  
# reproducible, make sure you lock down to a specific version, not  
# to latest! See  
# https://github.com/phusion/baseimage-docker/blob/master/Changelog.md  
# for a list of version numbers.  
FROM phusion/baseimage:0.9.17  
MAINTAINER Eike Hirsch <eike.hirsch@smartsteuer.de>  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# ...put your own build instructions here...  
ENV CLEWARECONTROL_VERSION 4.0.0  
# we have to compile the clewarecontrol sources.  
# Therefor we need a compiler and other dependencies  
RUN apt-get update && \  
apt-get -y install \  
build-essential \  
libhidapi-dev \  
pkg-config \  
wget  
  
# download the latest distro  
RUN wget
https://github.com/flok99/clewarecontrol/archive/${CLEWARECONTROL_VERSION}.tar.gz  
# unpack  
RUN tar xzf ${CLEWARECONTROL_VERSION}.tar.gz  
  
# comile  
RUN cd clewarecontrol-${CLEWARECONTROL_VERSION} && \  
make install  
  
# now that we have the executable we can delete everything else again.  
RUN apt-get -y --purge remove \  
build-essential \  
pkg-config \  
wget  
  
RUN apt-get -y autoremove  
  
RUN rm -r clewarecontrol-${CLEWARECONTROL_VERSION}  
  
# ...put your own build instructions here... END  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

