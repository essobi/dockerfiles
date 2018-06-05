FROM debian:testing  
  
MAINTAINER Phillip Labuschagne <philliplab@gmail.com>  
  
RUN apt-get update && apt-get install -y autoconf \  
build-essential \  
libtool \  
unzip \  
wget \  
zlib1g-dev \  
zlibc  
  
# Download and install latest version of ramics  
RUN wget --no-check-certificate
https://github.com/ramics/ramics/archive/master.zip \  
&& unzip master.zip  
  
RUN cd /ramics-master \  
&& autoreconf --install \  
&& ./configure \  
&& make \  
&& make install  
  

