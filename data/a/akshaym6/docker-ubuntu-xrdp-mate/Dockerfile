FROM akshaym6/docker-ubuntu-xrdp:16.04  
  
MAINTAINER Akshay Mohite <akksmohite@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -y && \  
apt-get install -y mate-core mate-desktop-environment mate-notification-daemon
gconf-service libnspr4 libnss3 fonts-liberation \  
libappindicator1 libcurl3 fonts-wqy-microhei firefox && \  
apt-get autoclean && apt-get autoremove && \  
rm -rf /var/lib/apt/lists/* && \  
echo "mate-session" > /home/xrdpuser/.xsession  

