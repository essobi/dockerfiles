FROM phusion/baseimage  
MAINTAINER Kaiden Prince  
  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash - && \  
apt-get install -y nodejs python  
  
VOLUME /data  
WORKDIR /data  
RUN useradd nodejs -m -s /bin/bash && usermod -p '*' nodejs  
ADD service /etc/service  
  
RUN chmod +x /etc/service/*/run

