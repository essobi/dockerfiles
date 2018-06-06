############################################################  
# Dockerfile to manage certificates  
# https://github.com/Unixono/docker-certs-manager  
############################################################  
FROM ubuntu:trusty  
MAINTAINER Facundo Victor <facundovt@gmail.com>  
ENV IMG_VER v0.0.1  
  
# Install dependencies  
RUN echo "deb http://archive.ubuntu.com/ubuntu/ $(lsb_release -sc) main
universe" >> /etc/apt/sources.listi \  
&& apt-get update \  
&& apt-get install -y python openssl  
  
# Path where the keys, csrs, certs and challenges will be stored  
ENV WORKDIR_PATH /var/letsencrypt  
RUN mkdir -p $WORKDIR_PATH  
  
# Grant permissions to the working directory  
RUN chmod 755 $WORKDIR_PATH  
  
# Copy the scripts  
COPY manage_certs.sh /acme/manage_certs.sh  
COPY acme-tiny /acme/acme-tiny  
  
# Change scripts permissions  
RUN chmod 755 /acme  
  
# Sets the default working directory  
WORKDIR /acme  
  
# Sets the default script  
ENTRYPOINT [ "/acme/manage_certs.sh" ]  

