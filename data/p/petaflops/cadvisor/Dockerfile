from google/cadvisor:v0.25.0  
MAINTAINER pro zpang  
  
# time  
RUN apk add --update tzdata && rm -rf /var/cache/apk/*  
RUN cp /usr/share/zoneinfo/Hongkong /etc/localtime  
  
# add gnu find  
RUN apk add --update findutils && rm -rf /var/cache/apk/*  

