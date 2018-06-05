##  
# Minimalist Docker Container for PSPNET_ADHOCCTL_SERVER  
# Built for Pterodactyl Panel  
#  
# MIT Licensed  
##  
FROM ubuntu:15.10  
MAINTAINER Belldandu, <kami@ilp.moe>  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install Dependencies  
RUN apt-get update  
RUN apt-get install -y git gcc libsqlite3-dev make curl ca-certificates
openssl  
  
RUN useradd -m -d /home/container container  
  
USER container  
ENV HOME /home/container  
  
WORKDIR /home/container  
  
COPY ./start.sh /start.sh  
  
CMD ["/bin/bash", "/start.sh"]  

