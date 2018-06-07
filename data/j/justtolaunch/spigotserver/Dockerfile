FROM openjdk:8-jre-alpine  
MAINTAINER justtolaunch  
  
VOLUME ["/data"]  
  
COPY start.sh /start.sh  
  
RUN apk update \  
&& apk add --no-cache sqlite \  
&& apk add --no-cache socat \  
&& adduser -D -h /data minecraft \  
&& chmod +x start.sh  
  
EXPOSE 25565  
CMD ["/start.sh"]  

