FROM ubuntu:14.04  
  
MAINTAINER Ben Heasly <benjamin.heasly@gmail.com>  
  
RUN apt-get update \  
&& apt-get install -y dcraw exrtools openexr \  
&& apt-get clean \  
&& apt-get autoclean \  
&& apt-get autoremove  
  
CMD ["echo", "exrtools - a collection of utilities for manipulating OpenEXR
images: http://scanline.ca/exrtools/"]  
  

