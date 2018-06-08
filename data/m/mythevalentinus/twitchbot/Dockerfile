FROM php:7.1.6-cli  
  
MAINTAINER Valentin Deville <contact@valentin-deville.eu>  
  
VOLUME /bot  
  
WORKDIR /root/  
COPY entrypoint.sh .  
  
RUN apt-get update && apt-get install -y git  
  
ENTRYPOINT /root/entrypoint.sh  

