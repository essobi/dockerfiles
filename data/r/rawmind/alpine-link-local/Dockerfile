FROM rawmind/alpine-base:3.5-1  
MAINTAINER Raul Sanchez <rawmind@gmail.com>  
  
ADD root /  
RUN chmod +x /start.sh && \  
apk add --no-cache iproute2  
  
ENTRYPOINT ["/start.sh"]  

