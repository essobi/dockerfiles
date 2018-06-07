FROM ubuntu  
  
MAINTAINER zopanix <zopanix@gmail.com>  
  
COPY resources /resources  
  
RUN resources/build && rm -rf resources  
  
VOLUME /data  
  
WORKDIR /data  

