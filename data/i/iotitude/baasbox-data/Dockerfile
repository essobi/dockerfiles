# Dockerfile for creating a data volume image used by the main BaasBox image  
FROM debian:jessie  
MAINTAINER Ruben Laube-Pohto  
  
RUN mkdir -p /usr/src/baasbox-db  
VOLUME /usr/src/baasbox/db /usr/src/baasbox/db  
CMD ["echo", "Data container for BaasBox"]  

