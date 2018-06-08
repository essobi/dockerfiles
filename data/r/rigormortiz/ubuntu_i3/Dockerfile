FROM rigormortiz/ubuntu_novnc:zesty  
  
MAINTAINER Mike Ortiz <mike@jellydice.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -y && \  
apt-get install -y vim i3 libnspr4 libnss3 fonts-liberation \  
libappindicator1 libcurl3 fonts-wqy-microhei firefox && \  
apt-get autoclean && apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
COPY supervisor_ubuntu_i3.conf /etc/supervisor/conf.d/ubuntu_i3.conf  

