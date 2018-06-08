# VERSION 0.1  
# DOCKER-VERSION 0.10.0  
# AUTHOR Saulo Alves <sauloal@gmail.com>  
# DESCRIPTION ubuntu updated  
# TO BUILD docker build -t sauloal/ubuntu14.04:20140516 .  
# docker tag 23f9f81618ce sauloal/ubuntu14.04:latest  
# TO UPLOAD while true; do docker push sauloal/ubuntu:14.04_20140516; echo $?;
if [ $? == "0" ]; then exit 0; fi; done  
# TO RUN  
FROM quintenk/supervisor  
  
MAINTAINER Saulo Alves <sauloal@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEBIAN_PRIORITY critical  
ENV DEBCONF_NOWARNINGS yes  
RUN apt-get update -y; \  
apt-get upgrade -y;  
  

