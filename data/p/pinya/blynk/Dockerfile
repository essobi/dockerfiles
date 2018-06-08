FROM openjdk:9-jre-slim  
MAINTAINER Sergei Silnov <po@kumekay.com>  
  
ENV VERSION 0.30.2  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-url="https://github.com/pinya/blynk-server.git" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.schema-version="1.0.0-rc1" \  
org.label-schema.version=$VERSION  
  
RUN apt-get update  
RUN apt-get install wget -y  
RUN mkdir /blynk  
RUN wget https://github.com/blynkkk/blynk-
server/releases/download/v${VERSION}/server-${VERSION}.jar -O
/blynk/server.jar  
  
# Create data folder. To persist data, map a volume to /data  
RUN mkdir /data  
  
# IP port listing:  
# 8442: Hardware plain tcp/ip port  
# 8441: Hardware ssl/tls port (for hardware that supports SSL/TLS sockets)  
# 8081: Web socket ssl/tls port  
# 8082: Web sockets plain tcp/ip port  
# 9443: Application mutual ssl/tls port  
# 8080: HTTP port  
# 7443: Administration UI HTTPS port  
EXPOSE 7443 8080 8081 8082 8441 8442 9443  
WORKDIR /data  
ENTRYPOINT ["java", "-jar", "/blynk/server.jar", "-dataFolder", "/data",
"-serverConfig", "/data/server.properties"]  

