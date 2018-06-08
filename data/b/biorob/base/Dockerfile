FROM ubuntu:14.04  
MAINTAINER Alexandre Tuleu <alexandre.tuleu.2005@polytechnique.org>  
RUN apt-get update && apt-get -y install wget \  
apt-transport-https \  
git  
RUN mkdir -p /etc/apt/sources.list.d  
RUN echo "deb https://ponyo.epfl.ch/packages trusty main" >>
/etc/apt/sources.list.d/ponyo.epfl.ch.list  
RUN wget -O - https://ponyo.epfl.ch/packages/sign.key | apt-key add -  

