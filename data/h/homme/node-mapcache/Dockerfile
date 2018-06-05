##  
# Node Mapcache  
#  
# This creates an Ubuntu derived base image that installs a recent  
# version of Node.js as well as the latest repository checkouts of  
# Mapserver Mapcache and the Node Mapcache bindings. Mapcache has a  
# broad range of compile time options enabled and as such this  
# provides a suitable base image for both experimenting with and  
# deriving production ready images from.  
#  
FROM ubuntu:quantal  
  
MAINTAINER Homme Zwaagstra <hrz@geodata.soton.ac.uk>  
  
# Ensure the package repository is up to date  
RUN echo "deb http://archive.ubuntu.com/ubuntu quantal main universe" >
/etc/apt/sources.list  
RUN apt-get update  
  
# Install Node.js  
RUN apt-get install -y software-properties-common python-software-properties
python g++ make cmake  
RUN add-apt-repository -y ppa:chris-lea/node.js  
RUN apt-get update  
RUN apt-get install -y nodejs  
  
# Install mapcache dependencies provided by Ubuntu repositories  
RUN apt-get install -y git \  
libaprutil1-dev \  
libapr1-dev \  
libpng12-dev \  
libjpeg-dev \  
libcurl4-gnutls-dev \  
libpcre3-dev \  
libpixman-1-dev \  
libgdal-dev \  
libgeos-dev \  
libsqlite3-dev \  
libdb-dev \  
libtiff4-dev  
  
# Install Mapcache itself  
RUN git clone https://github.com/mapserver/mapcache/ /usr/local/src/mapcache  
RUN mkdir /usr/local/src/mapcache/build && \  
cd /usr/local/src/mapcache/build && \  
cmake ../ -DWITH_FCGI=0 -DWITH_APACHE=0 -DWITH_PCRE=1 -DWITH_TIFF=1
-DWITH_BERKELEY_DB=1 -DWITH_MEMCACHE=1 && \  
make && \  
make install  
  
# Install Node Mapcache. This installs to `/node_modules` so will always be
found  
RUN git clone https://github.com/geo-data/node-mapcache/ /usr/local/src/node-
mapcache  
RUN npm config set mapcache:build_dir /usr/local/src/mapcache/build && \  
npm install /usr/local/src/node-mapcache  
  
# Run the Node Mapcache tests by default  
CMD npm test mapcache  

