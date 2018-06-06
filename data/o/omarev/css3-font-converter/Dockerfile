FROM ubuntu:precise  
MAINTAINER Nikita Omarev <nikita@omarev.com>  
  
# make sure the package repository is up to date  
RUN echo "deb http://archive.ubuntu.com/ubuntu raring main universe" >
/etc/apt/sources.list  
RUN apt-get update  
RUN mkdir -p /build  
RUN apt-get install -y fontforge wget tar build-essential  
RUN fakeroot apt-get install -y openjdk-7-jdk  
  
## ttf2eot build  
RUN cd /build && wget --no-check-certificate
https://ttf2eot.googlecode.com/files/ttf2eot-0.0.2-2.tar.gz && tar zxvf
ttf2eot-0.0.2-2.tar.gz  
RUN sed -i.bak "/using std::vector;/ i\\#include <cstddef>"
/build/ttf2eot-0.0.2-2/OpenTypeUtilities.h  
RUN cd /build/ttf2eot-0.0.2-2 && make && cp ttf2eot /usr/local/bin/ttf2eot  
  
## woff build  
RUN apt-get install -y unzip zlib1g-dev  
RUN cd /build && wget http://people.mozilla.org/~jkew/woff/woff-code-
latest.zip && unzip -d woff-code-latest woff-code-latest.zip  
RUN cd /build/woff-code-latest && make && cp sfnt2woff
/usr/local/bin/sfnt2woff  
  
## ttfautohint build  
RUN apt-get install -y libqt4-core libqt4-dev libqt4-gui qt4-dev-tools  
RUN apt-get install -y libfreetype6-dev  
RUN cd /build && wget
http://downloads.sourceforge.net/project/freetype/ttfautohint/0.97/ttfautohint-0.97.tar.gz
&& tar zxvf ttfautohint-0.97.tar.gz  
RUN cd /build/ttfautohint-0.97 && ./configure --without-doc && make install  
  
## CSS3FontConverter  
RUN apt-get install -y git  
RUN git clone https://github.com/zoltan-dulac/css3FontConverter  

