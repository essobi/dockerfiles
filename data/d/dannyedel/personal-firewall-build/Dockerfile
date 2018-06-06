FROM debian:jessie  
  
MAINTAINER Danny Edel <mail@danny-edel.de>  
  
# Use the US mirror, since this will auto-build in the docker cloud  
RUN sed -e 's|httpredir.debian.org|ftp.us.debian.org|g' -i
/etc/apt/sources.list  
  
RUN apt-get -yq update  
RUN apt-get -yq install \  
libnetfilter-queue-dev \  
build-essential \  
cmake \  
libboost-all-dev  
RUN apt-get -yq install ccache  

