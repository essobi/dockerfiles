FROM openjdk:8u121-jre-alpine  
MAINTAINER Oumar Aziz OUATTARA (wattazoum)  
  
RUN apk update && apk add fontconfig ttf-dejavu  
  
RUN adduser -S -u 1000 springboot && \  
mkdir -p /app && \  
chown -R springboot /app  
  
ADD entrypoint.sh /usr/local/bin/  
  
USER springboot  
  
WORKDIR /app  
  
VOLUME /app  
EXPOSE 8080  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
  

