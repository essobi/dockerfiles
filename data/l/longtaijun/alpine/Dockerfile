FROM alpine  
ENV REFRESHED_AT 2016-10-22  
MAINTAINER from www.svipc.com by tyson (longtaijun@msn.cn)  
  
RUN apk update && apk \--no-cache upgrade && \  
apk add \--no-cache make bash curl openssh wget vim && \  
rm -rf /var/cache/apk/*  
  
ENV TREM=linux  

