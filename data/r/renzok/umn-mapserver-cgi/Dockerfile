FROM debian:jessie  
MAINTAINER Renzo Kottmann <renzo.rkottman@gmail.com>  
  
ENV MAPSERVER_VERSION=6.4.1-5+b3  
ENV MAP_DIR=/mapserver/map  
ENV LANG C.UTF-8  
# Update and upgrade system  
RUN apt-get -qq update --fix-missing && \  
apt-get install -y \  
cgi-mapserver=${MAPSERVER_VERSION} \  
mapserver-bin=${MAPSERVER_VERSION}  
  
RUN mkdir -p ${MAP_DIR}  
  
VOLUME ${MAP_DIR}  
  
ENTRYPOINT ["/usr/lib/cgi-bin/mapserv"]  

