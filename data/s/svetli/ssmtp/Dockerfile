FROM alpine:latest  
  
MAINTAINER Svetli Nikolov  
  
# Install packages  
RUN apk add --no-cache --repository http://dl-
cdn.alpinelinux.org/alpine/edge/testing ssmtp  
  
# Cleanup  
RUN rm -rf \  
/var/cache/apk/* \  
/usr/share/doc \  
/usr/share/man  
  
# Copy config file  
COPY ssmtp.conf /etc/ssmtp/ssmtp.conf  

