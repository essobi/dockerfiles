FROM ubuntu:14.04  
MAINTAINER Ben Keith <keitwb@gmail.com>  
  
env DEBIAN_FRONTEND=noninteractive  
RUN apt-get update -y -qq && \  
apt-get install -y -qq wget python xdg-utils imagemagick && \  
apt-get clean  
  
RUN groupadd -r calibre && useradd -g calibre -d /opt/calibre -r -m calibre  
  
WORKDIR /tmp  
ENV CALIBRE_PACKAGE_URL http://download.calibre-
ebook.com/2.59.0/calibre-2.59.0-x86_64.txz  
RUN wget $CALIBRE_PACKAGE_URL &&\  
apt-get install -y -qq xz-utils &&\  
tar xvf calibre*.txz -C /opt/calibre &&\  
rm calibre*.txz &&\  
chown calibre:calibre -R /opt/calibre &&\  
apt-get remove -y -qq xz-utils &&\  
apt-get clean  
  
RUN mkdir /calibre-library &&\  
chown calibre:calibre /calibre-library  
  
VOLUME /calibre-library  

