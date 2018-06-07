# Minimal Minecraft Docker container for Pterodactyl Panel  
FROM openjdk:8-jre-alpine  
  
MAINTAINER Dane Everitt <dane+docker@daneeveritt.com>  
  
RUN apk update \  
&& apk upgrade \  
&& apk add \--no-cache --update curl ca-certificates openssl bash perl \  
&& adduser -D -h /home/container container  
  
USER container  
ENV  USER container  
ENV HOME /home/container  
  
WORKDIR /home/container  
  
COPY ./start.sh /start.sh  
  
CMD ["/bin/bash", "/start.sh"]  

