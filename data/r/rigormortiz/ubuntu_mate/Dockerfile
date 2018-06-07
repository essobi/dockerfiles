FROM rigormortiz/ubuntu_novnc:latest  
  
MAINTAINER Mike Ortiz <mike@jellydice.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -y && \  
apt-get install -y mate-core vim \  
mate-desktop-environment mate-notification-daemon \  
gconf-service libnspr4 libnss3 fonts-liberation \  
libappindicator1 libcurl3 fonts-wqy-microhei firefox && \  
apt-get autoclean && apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
COPY supervisor_mate.conf /etc/supervisor/conf.d/mate.conf  

