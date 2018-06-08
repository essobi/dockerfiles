FROM debian:jessie  
MAINTAINER sthysel <sthysel@gmail.com>  
ENV REFRESHED_AT 2015-07-29  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y --no-install-recommends \  
apt-transport-https \  
build-essential \  
libc6-i386 \  
lib32z1 \  
lib32ncurses5 \  
wget \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN env --unset=DEBIAN_FRONTEND  
  
RUN mkdir /rebol  
WORKDIR /rebol  
RUN wget http://www.rebol.com/downloads/v278/rebol-core-278-4-3.tar.gz -O
rebol.tgz && \  
tar xzvf rebol.tgz && \  
mv /rebol/releases/rebol-core/rebol /usr/bin/rebol  
  

