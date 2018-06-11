FROM debian  
MAINTAINER Zoar  
  
#apt update & Install nginx and busybox  
RUN apt-get update  
RUN apt-get install nginx busybox -y  
RUN mkdir -p /tmp/gsi/cache  
RUN mkdir -p /tmp/gsi/tmp  
  
#include nginx conf file  
ADD gsicache.conf /etc/nginx/conf.d/  
  
EXPOSE 8080  
CMD ["nginx", "-g", "daemon off;"]  

