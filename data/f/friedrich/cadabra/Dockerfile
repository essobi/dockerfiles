FROM debian:stable  
MAINTAINER Friedrich Schöller <code@schoeller.se>  
  
RUN apt-get update  
RUN apt-get -y install cadabra  
RUN rm -r /var/lib/apt/lists  
  
ADD http://mirrors.ctan.org/fonts/cm/ps-type1/bakoma/ttf/cmtt12.ttf
/usr/share/fonts/  

