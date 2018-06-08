###############################################################################################  
#  
# Dockerfile used to create base image for all the othe images with basic
debugging utilities.  
#  
###############################################################################################  
  
FROM alpine:3.7  
  
LABEL maintainer="rahuljain"  
  
ENV VERSION 1.0.0  
  
RUN apk add --no-cache --update bash py-pip supervisor drill ca-certificates
wget curl busybox busybox-extras unrar && \  
pip install --upgrade pip kazoo jinja2 && \  
mkdir /opt && \  
rm -rf /var/cache/apk/*  

