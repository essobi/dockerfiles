FROM pl31/debian:stretch  
MAINTAINER Patrick Büch <dh@paco.pl31.de>  
  
# install wine  
RUN echo "Europe/Berlin" > /etc/timezone && \  
dpkg-reconfigure tzdata && \  
dpkg --add-architecture i386 && \  
apt-get -y update && \  
apt-get -y upgrade && \  
apt-get -y install \  
wine-development \  
wine32-development \  
xvfb xauth  

