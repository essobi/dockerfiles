################################################  
# Dockerfile to build Platanus 1.2.4 software  
# Based on debian image  
################################################  
  
# Set the base image to debian blast  
FROM debian:latest  
  
# Set noninterative mode  
ENV DEBIAN_FRONTEND noninteractive  
ENV PACKAGES wget make gcc g++ mafft unzip  
  
ENV PLATANUS_BINARY http://platanus.bio.titech.ac.jp/?ddownload=145  
ENV PLATANUS_TRIM_BINARY http://platanus.bio.titech.ac.jp/?ddownload=153  
ENV PLATANUS_INTERNAL_TRIM_BINARY
http://platanus.bio.titech.ac.jp/?ddownload=154  
  
  
################## Update & upgrade ######################  
  
RUN apt-get update -y  
RUN apt-get install -y ${PACKAGES}  
  
################# Platanus install ########################  
  
RUN wget -O Platanus ${PLATANUS_BINARY}  
RUN cp Platanus /usr/local/bin/  
RUN chmod +x /usr/local/bin/Platanus  
  
RUN wget -O Platanus_trim ${PLATANUS_TRIM_BINARY}  
RUN cp Platanus_trim /usr/local/bin/  
RUN chmod +x /usr/local/bin/Platanus_trim  
  
RUN wget -O Platanus_internal_trim ${PLATANUS_TRIM_BINARY}  
RUN cp Platanus_internal_trim /usr/local/bin/  
RUN chmod +x /usr/local/bin/Platanus_internal_trim  
  
  
###############################################################  
  
MAINTAINER Monjeaud Cyril <Cyril.Monjeaud@irisa.fr>  

