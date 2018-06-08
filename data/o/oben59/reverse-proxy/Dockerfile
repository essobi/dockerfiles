# Docker image  
# Nginx reverse-proxy  
# @author oben59<benoit.oyez@telecomnancy.net>  
FROM jwilder/nginx-proxy:latest  
  
MAINTAINER oben59<benoit.oyez@telecomnancy.net>  
  
WORKDIR /app  
  
# Replace IP directive with container name for DNS resolution  
RUN sed 10s/Address.IP/Container.Name/ -i nginx.tmpl  
RUN sed 14s/Container.IP/Container.Name/ -i nginx.tmpl

