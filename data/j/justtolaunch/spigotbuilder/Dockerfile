FROM openjdk:8-jre-alpine  
MAINTAINER justtolaunch  
  
VOLUME ["/data"]  
  
COPY start.sh /start.sh  
  
RUN apk update && apk add --no-cache \  
wget \  
git \  
&& rm -rf /var/cache/apk/* \  
&& adduser -D -h /data builder \  
&& chmod +x start.sh  
  
CMD ["/start.sh"]  

