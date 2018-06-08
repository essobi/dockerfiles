FROM ubuntu:14.04  
MAINTAINER Ben Heasly <benjamin.heasly@gmail.com>  
  
### pbrt dependencies  
RUN apt-get update \  
&& apt-get install -y \  
bison \  
build-essential \  
flex \  
git \  
gsl-bin \  
libgsl0-dev \  
libpng12-dev \  
libjpeg-dev \  
libilmbase-dev \  
libopenexr-dev \  
&& apt-get clean \  
&& apt-get autoclean \  
&& apt-get autoremove  
  
### build and install PBRT  
RUN git clone https://github.com/ydnality/pbrt-v2-spectral.git  
WORKDIR pbrt-v2-spectral/src  
RUN make  
  
### install pbrt binaries  
RUN cp /pbrt-v2-spectral/src/bin/* /usr/local/bin  
  

