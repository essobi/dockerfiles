FROM node:7.4.0-alpine  
MAINTAINER Secopstech <info@secopstech.com>  
  
ADD ./socket.io /app  
  
RUN cd /app && npm install \  
&& cd chat && npm install  
  
COPY ./boot.sh /boot.sh  
CMD ["/bin/sh", "/boot.sh"]

