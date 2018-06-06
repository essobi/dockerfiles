############################################################  
# Dockerfile to build Swarm 2.1.5  
# Based on debian wheezy  
############################################################  
  
# Set the base image to debian wheezy  
FROM debian:wheezy  
  
# Set noninterative mode  
ENV DEBIAN_FRONTEND noninteractive  
ENV PACKAGES wget make cmake gcc g++ python-dev  
  
########################### FLASH URLS #############################  
  
ENV SWARM_SOURCE
https://github.com/torognes/swarm/releases/download/v2.1.5/swarm-2.1.5-linux-x86_64  
  
################## DEPENDENCIES INSTALLATION ######################  
  
RUN apt-get update -y  
RUN apt-get install -y ${PACKAGES}  
  
################## SWARM INSTALLATION ######################  
  
RUN wget ${SWARM_SOURCE} -O /usr/local/bin/swarm  
RUN chmod 755 /usr/local/bin/swarm  
  
###############################################################  
  
MAINTAINER Monjeaud Cyril <Cyril.Monjeaud@irisa.fr>  
  

